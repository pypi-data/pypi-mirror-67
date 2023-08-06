# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.
""":term:`compile` & :term:`execute` network graphs of operations."""
import copy
import logging
import random
import re
import sys
import time
from collections import ChainMap, abc, defaultdict, namedtuple
from functools import partial
from itertools import chain, count
from typing import (
    Any,
    Callable,
    Collection,
    List,
    Mapping,
    Optional,
    Tuple,
    Union,
)

import networkx as nx
from boltons.setutils import IndexedSet as iset

from .base import UNSET, Items, PlotArgs, Plottable, aslist, astuple, jetsam
from .config import (
    get_execution_pool,
    is_abort,
    is_debug,
    is_endure_operations,
    is_marshal_tasks,
    is_parallel_tasks,
    is_reschedule_operations,
    is_skip_evictions,
    first_solid,
)
from .modifiers import (
    is_mapped,
    is_optional,
    is_pure_sideffect,
    is_sideffect,
    is_sideffected,
    optional,
)
from .op import Operation

NodePredicate = Callable[[Any, Mapping], bool]

#: If this logger is *eventually* DEBUG-enabled,
#: the string-representation of network-objects (network, plan, solution)
#: is augmented with children's details.
log = logging.getLogger(__name__)


def _isDebugLogging():
    return log.isEnabledFor(logging.DEBUG)


class AbortedException(Exception):
    """
    Raised from Network when :func:`.abort_run()` is called, and contains the solution ...

    with any values populated so far.
    """


class IncompleteExecutionError(Exception):
    """
    Error report when any `netop` operations were canceled/failed.

    The exception contains 3 arguments:

    1. the causal errors and conditions (1st arg),
    2. the list of collected exceptions (2nd arg), and
    3. the solution instance (3rd argument), to interrogate for more.

    Returned by :meth:`.check_if_incomplete()` or raised by :meth:`.scream_if_incomplete()`.
    """

    def __str__(self):
        return self.args[0]  # pylint: disable=unsubscriptable-object


def _unsatisfied_operations(dag, inputs: Collection) -> List:
    """
    Traverse topologically sorted dag to collect un-satisfied operations.

    Unsatisfied operations are those suffering from ANY of the following:

    - They are missing at least one compulsory need-input.
        Since the dag is ordered, as soon as we're on an operation,
        all its needs have been accounted, so we can get its satisfaction.

    - Their provided outputs are not linked to any data in the dag.
        An operation might not have any output link when :meth:`_prune_graph()`
        has broken them, due to given intermediate inputs.

    :param dag:
        a graph with broken edges those arriving to existing inputs
    :param inputs:
        an iterable of the names of the input values
    :return:
        a list of unsatisfied operations to prune

    """
    # To collect data that will be produced.
    ok_data = set(inputs)
    # To collect the map of operations --> satisfied-needs.
    op_satisfaction = defaultdict(set)
    # To collect the operations to drop.
    unsatisfied = []
    # Topo-sort dag respecting operation-insertion order to break ties.
    sorted_nodes = nx.topological_sort(dag)
    for node in sorted_nodes:
        if isinstance(node, Operation):
            if not dag.adj[node]:
                # Prune operations that ended up providing no output.
                unsatisfied.append(node)
            else:
                # It's ok not to dig into edge-data("optional") here,
                # we care about all needs, including broken ones.
                real_needs = set(n for n in node.needs if not is_optional(n))
                if real_needs.issubset(op_satisfaction[node]):
                    # We have a satisfied operation; mark its output-data
                    # as ok.
                    ok_data.update(dag.adj[node])
                else:
                    # Prune operations with partial inputs.
                    unsatisfied.append(node)
        elif isinstance(node, str):  # `str` are givens
            if node in ok_data:
                # mark satisfied-needs on all future operations
                for future_op in dag.adj[node]:
                    op_satisfaction[future_op].add(node)
        else:
            raise AssertionError(f"Unrecognized network graph node {node}")

    return unsatisfied


class Solution(ChainMap, Plottable):
    """
    A chain-map collecting :term:`solution` outputs and execution state (eg :term:`overwrites`)
    """

    def __init__(self, plan, input_values: dict):
        #: An ordered mapping of plan-operations to their results
        #: (initially empty dicts).
        #: The result dictionaries pre-populate this (self) chainmap,
        #: with the 1st map (wins all reads) the last operation,
        #: the last one the `input_values` dict.
        self._layers = {op: {} for op in yield_ops(reversed(plan.steps))}
        super().__init__(*self._layers.values(), input_values)

        #: the plan that produced this solution
        self.plan = plan
        #: A dictionary with keys the operations executed, and values their status:
        #:
        #: - no key:            not executed yet
        #: - value None:        execution ok
        #: - value Exception:   execution failed
        #: - value Collection:  canceled provides
        self.executed = {}
        #: A sorted set of :term:`canceled operation`\\s due to upstream failures.
        self.canceled = iset()  # not iterated, order not important, but ...
        #: a flag controlled by `plan` (by invoking :meth:`finalized` is invoked)
        #: which becomes `True` when this instance has finished accepting results.
        self.finalized = False
        self.elapsed_ms = {}
        #: A unique identifier to distinguish separate flows in execution logs.
        self.solid = "%X" % random.randint(0, 2 ** 16)

        ## Cache context-var flags.
        #
        self.is_endurance = is_endure_operations()
        self.is_reschedule = is_reschedule_operations()
        self.is_parallel = is_parallel_tasks()
        self.is_marshal = is_marshal_tasks()

        #: Cloned from `plan` will be modified, by removing the downstream edges of:
        #:
        #: - any partial outputs not provided, or
        #: - all `provides` of failed operations.
        #:
        #: FIXME: SPURIOUS dag reversals on multi-threaded runs (see below next assertion)!
        self.dag = plan.dag.copy()
        # assert next(iter(dag.edges))[0] == next(iter(plan.dag.edges))[0]:

    def __copy__(self):
        clone = type(self)(self.plan, {})
        props = (
            "maps executed canceled finalized elapsed_ms solid _layers"
            " is_endurance is_reschedule is_parallel is_marshal dag"
        ).split()
        for p in props:
            setattr(clone, p, getattr(self, p))

        return clone

    def __repr__(self):
        if is_debug():
            return self.debugstr()
        else:
            items = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
            return f"{{{items}}}"

    def debugstr(self):
        return f"{type(self).__name__}({dict(self)}, {self.plan}, {self.executed}, {self._layers})"

    def _reschedule(self, dag, nbunch_to_break, op):
        """Update dag/canceled/executed ops and return newly-canceled ops. """
        dag.remove_edges_from(tuple(dag.out_edges(nbunch_to_break)))
        canceled = _unsatisfied_operations(dag, self)
        # Minus executed, bc partial-out op might not have any provides left.
        newly_canceled = iset(canceled) - self.canceled - self.executed
        self.canceled.update(newly_canceled)

        if newly_canceled and log.isEnabledFor(logging.INFO):
            reason = (
                "failure of"
                if isinstance(nbunch_to_break, Operation) > 1
                else "rescheduled"
            )
            log.info(
                "... (%s) CANCELING +%s ops%s due to %s of op(%s).",
                self.solid,
                len(newly_canceled),
                [n.name for n in newly_canceled],
                reason,
                op.name,
            )

    def operation_executed(self, op, outputs):
        """
        Invoked once per operation, with its results.

        It will update :attr:`executed` with the operation status and
        if `outputs` were partials, it will update :attr:`canceled`
        with the unsatisfied ops downstream of `op`.

        :param op:
            the operation that completed ok
        :param outputs:
            The named values the op` actually produced,
            which may be a subset of its `provides`.  Sideffects are not considered.

        """

        def collect_canceled_sideffects(dep, val) -> Collection:
            """Return any sfx `dep` with falsy value, singularizing sideffected."""
            if val or not is_sideffect(dep):
                return ()
            if is_pure_sideffect(dep):
                return (dep,)
            ## Singularize sideffected
            assert is_sideffected(dep), locals()
            return (dep.withset(sideffects=(s,)) for s in dep.sideffects)

        assert not self.finalized, f"Cannot reuse solution: {self}"
        self._layers[op].update(outputs)
        self.executed[op] = None

        if first_solid(self.is_reschedule, op.rescheduled):
            ## Find which provides have been broken?
            #
            # OPTIMIZE: could use _fn_provides
            missing_outs = iset(op.provides) - set(outputs)
            sfx = (out for out in missing_outs if is_sideffect(out))
            canceled_sideffects = [
                sf
                for k, v in outputs.items()
                for sf in collect_canceled_sideffects(k, v)
            ]
            to_break = (missing_outs - sfx) | canceled_sideffects
            log.info(
                "... (%s) missing partial outputs %s from rescheduled %s.",
                self.solid,
                list(to_break),
                op,
            )

            if to_break:
                self._reschedule(self.dag, to_break, op)
                # list used by `check_if_incomplete()`
                self.executed[op] = to_break

    def operation_failed(self, op, ex):
        """
        Invoked once per operation, with its results.

        It will update :attr:`executed` with the operation status and
        the :attr:`canceled` with the unsatisfied ops downstream of `op`.
        """
        assert not self.finalized, f"Cannot reuse solution: {self}"
        self.executed[op] = ex
        self._reschedule(self.dag, op, op)

    def finalize(self):
        """invoked only once, after all ops have been executed"""
        # Invert solution so that last value wins
        if not self.finalized:
            self.finalized = True

    def __delitem__(self, key):
        for d in self.maps:
            d.pop(key, None)

    def is_failed(self, op):
        return isinstance(self.executed.get(op), Exception)

    @property
    def overwrites(self) -> Mapping[Any, List]:
        """
        The data in the solution that exist more than once.

        A "virtual" property to a dictionary with keys the names of values that
        exist more than once, and values, all those values in a list, ordered:

        - before :meth:`finalized()`, as computed;
        - after :meth:`finalized()`, in reverse.
        """
        maps = self.maps
        dd = defaultdict(list)
        for d in maps:
            for k, v in d.items():
                dd[k].append(v)

        return {k: v for k, v in dd.items() if len(v) > 1}

    def check_if_incomplete(self) -> Optional[IncompleteExecutionError]:
        """Return a :class:`IncompleteExecutionError` if `netop` operations failed/canceled. """
        failures = {
            op: ex for op, ex in self.executed.items() if isinstance(ex, Exception)
        }
        incomplete = iset(chain(self.canceled, failures.keys()))
        if incomplete:
            incomplete = [op.name for op in incomplete]
            partial_msgs = {
                f"\n  +--{op.name}: {list(pouts)}"
                for op, pouts in self.executed.items()
                if pouts and isinstance(pouts, abc.Collection)
            }
            err_msgs = [
                f"\n  +--{op.name}: {type(ex).__name__}('{ex}')"
                for op, ex in failures.items()
            ]
            msg = (
                f"Not completed x{len(incomplete)} operations {list(incomplete)}"
                f" due to x{len(failures)} failures and x{len(partial_msgs)} partial-ops:"
                f"{''.join(err_msgs)}{''.join(partial_msgs)}"
            )
            return IncompleteExecutionError(msg, self)

    def scream_if_incomplete(self):
        """Raise a :class:`IncompleteExecutionError` if `netop` operations failed/canceled. """
        ex = self.check_if_incomplete()
        if ex:
            raise ex

    def prepare_plot_args(self, plot_args: PlotArgs) -> PlotArgs:
        """delegate to plan, with solution"""
        name = f"solution-x{len(self.plan.net.graph.nodes)}-nodes"
        plot_args = plot_args.with_defaults(name=name, solution=self)
        plot_args = self.plan.prepare_plot_args(plot_args)
        plot_args = plot_args._replace(plottable=self)

        return plot_args


class _EvictInstruction(str):
    """
    A step in the ExecutionPlan to evict a computed value from the `solution`.

    It's a step in :attr:`ExecutionPlan.steps` for the data-node `str` that
    frees its data-value from `solution` after it is no longer needed,
    to reduce memory footprint while computing the graph.
    """

    __slots__ = ()  # avoid __dict__ on instances

    def __repr__(self):
        return f"EvictInstruction('{self}')"


def _yield_datanodes(nodes):
    """May scan dag nodes."""
    return (n for n in nodes if isinstance(n, str))


def yield_ops(nodes):
    """May scan (preferably)  ``plan.steps`` or dag nodes."""
    return (n for n in nodes if isinstance(n, Operation))


def yield_node_names(nodes):
    """Yield either ``op.name`` or ``str(node)``."""
    return (str(getattr(n, "name", n)) for n in nodes)


def _optionalized(graph, data):
    """Retain optionality of a `data` node based on all `needs` edges."""
    all_optionals = all(e[2] for e in graph.out_edges(data, "optional", False))
    return (
        optional(data)
        if all_optionals
        else data  # sideffect
        if is_sideffect(data)
        else str(data)  # un-optionalize
    )


def collect_requirements(graph) -> Tuple[iset, iset]:
    """Collect & split datanodes in (possibly overlapping) `needs`/`provides`."""
    operations = list(yield_ops(graph))
    provides = iset(
        p for op in operations for p in getattr(op, "op_provides", op.provides)
    )
    needs = iset(_optionalized(graph, n) for op in operations for n in op.needs)
    provides = iset(provides)
    return needs, provides


class _OpTask:
    """
    Mimic :class:`concurrent.futures.Future` for :term:`sequential` execution.

    This intermediate class is needed to solve pickling issue with process executor.
    """

    __slots__ = ("op", "sol", "result", "solid")
    logname = __name__

    def __init__(self, op, sol, solid):
        self.op = op
        self.sol = sol
        self.result = UNSET
        self.solid = solid

    def marshalled(self):
        import dill

        return dill.dumps(self)

    def __call__(self):
        if self.result == UNSET:
            self.result = None
            log = logging.getLogger(self.logname)
            log.debug("+++ (%s) Executing %s...", self.solid, self)
            self.result = self.op.compute(self.sol)

        return self.result

    get = __call__

    def __repr__(self):
        try:
            sol_items = list(self.sol)
        except Exception:
            sol_items = type(self.sol).__name__
        return f"OpTask({self.op}, sol_keys={sol_items!r})"


def _do_task(task):
    """
    Un-dill the *simpler* :class:`_OpTask` & Dill the results, to pass through pool-processes.

    See https://stackoverflow.com/a/24673524/548792
    """
    ## Note, the "else" case is only for debugging aid,
    #  by skipping `_OpTask.marshal()`` call.
    #
    if isinstance(task, bytes):
        import dill

        task = dill.loads(task)
        result = task()
        result = dill.dumps(result)
    else:
        result = task()

    return result


class ExecutionPlan(
    namedtuple("ExecPlan", "net needs provides dag steps asked_outs"), Plottable
):
    """
    A pre-compiled list of operation steps that can :term:`execute` for the given inputs/outputs.

    It is the result of the network's :term:`compilation` phase.

    Note the execution plan's attributes are on purpose immutable tuples.

    .. attribute:: net

        The parent :class:`Network`
    .. attribute:: needs

        An :class:`.IndexedSet` with the input names needed to exist in order to produce all `provides`.
    .. attribute:: provides

        An :class:`.IndexedSet` with the outputs names produces when all `inputs` are given.
    .. attribute:: dag

        The regular (not broken) *pruned* subgraph of net-graph.
    .. attribute:: steps

        The tuple of operation-nodes & *instructions* needed to evaluate
        the given inputs & asked outputs, free memory and avoid overwriting
        any given intermediate inputs.
    .. attribute:: asked_outs

        When true, :term:`evictions` may kick in (unless disabled by :term:`configurations`),
        otherwise, *evictions* (along with prefect-evictions check) are skipped.
    """

    def prepare_plot_args(self, plot_args: PlotArgs) -> PlotArgs:
        plot_args = plot_args.clone_or_merge_graph(self.net.graph)
        graph = plot_args.graph

        clusters = None
        if self.dag.nodes != graph.nodes:
            clusters = {n: "after pruning" for n in self.dag.nodes}

        plot_args = plot_args.with_defaults(
            name=f"plan-x{len(graph.nodes)}-nodes",
            steps=self.steps,
            inputs=self.needs,
            outputs=self.provides,
            clusters=clusters,
        )
        plot_args = plot_args._replace(plottable=self)

        return plot_args

    def __repr__(self):
        needs = aslist(self.needs, "needs")
        provides = aslist(self.provides, "provides")
        steps = (
            "".join(f"\n  +--{s}" for s in self.steps)
            if is_debug()
            else ", ".join(yield_node_names(self.steps))
        )
        return f"ExecutionPlan(needs={needs}, provides={provides}, x{len(self.steps)} steps: {steps})"

    def validate(self, inputs: Items, outputs: Items):
        """
        Scream on invalid inputs, outputs or no operations in graph.

        :raises ValueError:
            - If cannot produce any `outputs` from the given `inputs`, with msg:

                *Unsolvable graph: ...*

            - If given `inputs` mismatched plan's :attr:`needs`, with msg:

                *Plan needs more inputs...*

            - If net cannot produce asked `outputs`, with msg:

                *Unreachable outputs...*

        """
        if not self.dag:
            raise ValueError(f"Unsolvable graph:\n  {self}")

        # Check plan<-->inputs mismatch.
        #
        missing = iset(self.needs) - set(inputs)
        if missing:
            raise ValueError(
                f"Plan needs more inputs: {list(missing)}"
                f"\n  given inputs: {list(inputs)}\n  {self}"
            )

        if outputs:
            unknown = (
                iset(astuple(outputs, "outputs", allowed_types=abc.Sequence))
                - self.provides
            )
            if unknown:
                raise ValueError(
                    f"Unreachable outputs {list(unknown)}\n  for given inputs {list(unknown)}"
                    f"\n for graph: {self}\n  {self}"
                )

    def _check_if_aborted(self, solution):
        if is_abort():
            raise AbortedException(solution)

    def _prepare_tasks(
        self, operations, solution, pool, global_parallel, global_marshal
    ) -> Union["Future", _OpTask, bytes]:
        """
        Combine ops+inputs, apply :term:`marshalling`, and submit to :term:`execution pool` (or not) ...

         based on global/pre-op configs.
        """
        ## Selectively DILL the *simpler* _OpTask & `sol` dict
        #  so as to pass through pool-processes,
        #  (s)ee https://stackoverflow.com/a/24673524/548792)
        #  and handle results in this thread, to evade Solution locks.
        #
        input_values = dict(solution)

        def prep_task(op):
            try:
                # Mark start time here, to include also marshalling overhead.
                solution.elapsed_ms[op] = time.time()

                task = _OpTask(op, input_values, solution.solid)
                if first_solid(global_marshal, op.marshalled):
                    task = task.marshalled()

                if first_solid(global_parallel, op.parallel):
                    if not pool:
                        raise RuntimeError(
                            "With `parallel` you must `set_execution_pool().`"
                        )

                    task = pool.apply_async(_do_task, (task,))
                elif isinstance(task, bytes):
                    # Marshalled (but non-parallel) tasks still need `_do_task()`.
                    task = partial(_do_task, task)
                    task.get = task.__call__

                return task
            except Exception as ex:
                jetsam(ex, locals(), "task", plan="self")
                raise

        return [prep_task(op) for op in operations]

    def _handle_task(self, future, op, solution) -> None:
        """Un-dill parallel task results (if marshalled), and update solution / handle failure."""

        def elapsed_ms(op):
            t0 = solution.elapsed_ms[op]
            solution.elapsed_ms[op] = elapsed = round(1000 * (time.time() - t0), 3)

            return elapsed

        try:
            ## Reset start time for Sequential tasks
            #  (bummer, they will miss marshalling overhead).
            #
            if isinstance(future, _OpTask):
                solution.elapsed_ms[op] = time.time()

            outputs = future.get()
            if isinstance(outputs, bytes):
                import dill

                outputs = dill.loads(outputs)

            solution.operation_executed(op, outputs)

            elapsed = elapsed_ms(op)
            log.debug(
                "... (%s) op(%s) completed in %sms.", solution.solid, op.name, elapsed
            )
        except Exception as ex:
            is_endured = first_solid(solution.is_endurance, op.endured)
            elapsed = elapsed_ms(op)
            loglevel = logging.WARNING if is_endured else logging.DEBUG
            log.log(
                loglevel,
                "... (%s) %s op(%s) FAILED in %0.3fms, due to: %s(%s)",
                solution.solid,
                "*Enduring* " if is_endured else "",
                op.name,
                elapsed,
                type(ex).__name__,
                ex,
            )

            if is_endured:
                solution.operation_failed(op, ex)
            else:
                # Although `plan` have added to jetsam in `compute()``,
                # add it again, in case compile()/execute() is called separately.
                jetsam(ex, locals(), "solution", task="future", plan="self")
                raise

    def _execute_thread_pool_barrier_method(self, solution: Solution):
        """
        This method runs the graph using a parallel pool of thread executors.
        You may achieve lower total latency if your graph is sufficiently
        sub divided into operations using this method.

        :param solution:
            must contain the input values only, gets modified
        """
        pool = get_execution_pool()  # cache pool
        parallel = solution.is_parallel
        marshal = solution.is_marshal

        # with each loop iteration, we determine a set of operations that can be
        # scheduled, then schedule them onto a thread pool, then collect their
        # results onto a memory solution for use upon the next iteration.
        while True:
            ## Note: do not check abort in between task handling (at the bottom),
            #  or it would ignore solution updates from already executed tasks.
            self._check_if_aborted(solution)

            # the upnext list contains a list of operations for scheduling
            # in the current round of scheduling
            upnext = []
            # TODO: optimization: start batches from previous last op).
            for node in self.steps:
                ## Determines if a Operation is ready to be scheduled for execution
                #  based on what has already been executed.
                if (
                    isinstance(node, Operation)
                    and node not in solution.executed
                    and set(yield_ops(nx.ancestors(self.dag, node))).issubset(
                        solution.executed
                    )
                ):
                    if node not in solution.canceled:
                        upnext.append(node)
                elif isinstance(node, _EvictInstruction):
                    # Only evict if all successors for the data node
                    # have been executed.
                    if (
                        # An optional need may not have a value in the solution.
                        node in solution
                        and (
                            # The 2nd eviction branch for unused provides.
                            node not in self.dag.nodes
                            # Scan node's successors in `broken_dag`, not to block
                            # an op waiting for calced data already given as input.
                            or set(self.dag.successors(node)).issubset(
                                solution.executed
                            )
                        )
                    ):
                        if _isDebugLogging():
                            log.debug(
                                "... (%s) evicting '%s' from solution%s.",
                                solution.solid,
                                node,
                                list(solution),
                            )
                        del solution[node]

            # stop if no nodes left to schedule, exit out of the loop
            if not upnext:
                ## Re-check evictions and assume all ops executed.
                #  Sequenced executor has no such problem bc exhausts steps.
                #
                #  TODO: evictions for parallel are wasting loops.
                #
                for node in self.steps:
                    if isinstance(node, _EvictInstruction) and node in solution:
                        del solution[node]
                break

            if _isDebugLogging():
                log.debug(
                    "+++ (%s) Parallel batch%s on solution%s.",
                    solution.solid,
                    list(op.name for op in upnext),
                    list(solution),
                )
            tasks = self._prepare_tasks(upnext, solution, pool, parallel, marshal)

            ## Handle results.
            #
            for op, task in zip(upnext, tasks):
                self._handle_task(task, op, solution)

    def _execute_sequential_method(self, solution: Solution):
        """
        This method runs the graph one operation at a time in a single thread

        :param solution:
            must contain the input values only, gets modified
        """
        for step in self.steps:
            self._check_if_aborted(solution)

            if isinstance(step, Operation):
                if step in solution.canceled:
                    continue

                task = _OpTask(step, solution, solution.solid)
                self._handle_task(task, step, solution)

            elif isinstance(step, _EvictInstruction):
                # Cache value may be missing if it is optional.
                if step in solution:
                    log.debug(
                        "... (%s) evicting '%s' from solution%s.",
                        solution.solid,
                        step,
                        list(solution),
                    )
                    del solution[step]

            else:
                raise AssertionError(f"Unrecognized instruction.{step}")

    def execute(self, named_inputs, outputs=None, *, name="") -> Solution:
        """
        :param named_inputs:
            A mapping of names --> values that must contain at least
            the compulsory inputs that were specified when the plan was built
            (but cannot enforce that!).
            Cloned, not modified.
        :param outputs:
            If not None, they are just checked if possible, based on :attr:`provides`,
            and scream if not.

        :return:
            The :term:`solution` which contains the results of each operation executed
            +1 for inputs in separate dictionaries.

        :raises ValueError:
            - If plan does not contain any operations, with msg:

                *Unsolvable graph: ...*

            - If given `inputs` mismatched plan's :attr:`needs`, with msg:

                *Plan needs more inputs...*

            - If net cannot produce asked `outputs`, with msg:

                *Unreachable outputs...*
        """
        try:
            self.validate(named_inputs, outputs)

            ## Choose a method of execution
            #
            in_parallel = is_parallel_tasks() or any(
                op.parallel for op in yield_ops(self.steps)
            )
            executor = (
                self._execute_thread_pool_barrier_method
                if in_parallel
                else self._execute_sequential_method
            )

            # If certain outputs asked, put relevant-only inputs in solution,
            # otherwise, keep'em all.
            #
            evict = self.asked_outs and not is_skip_evictions()
            # Note: clone and keep original `inputs` in the 1st chained-map.
            solution = Solution(
                self,
                {k: v for k, v in named_inputs.items() if k in self.dag.nodes}
                if evict
                else named_inputs,
            )

            log.debug(
                "=== (%s) Executing netop(%s)%s%s, on inputs%s, according to %s...",
                solution.solid,
                name,
                ", in parallel" if in_parallel else "",
                ", evicting" if evict else "",
                list(solution),
                self,
            )

            try:
                executor(solution)
            finally:
                solution.finalize()

                ## Log cumulative operations elapsed time.
                #
                if _isDebugLogging():
                    elapsed = sum(solution.elapsed_ms.values())
                    log.debug(
                        "=== (%s) Completed netop(%s) in %0.3fms.",
                        solution.solid,
                        name,
                        elapsed,
                    )

            # Validate eviction was perfect
            #
            if evict:
                expected_provides = set(
                    n.sideffected if is_sideffected(n) else n for n in self.provides
                )
                # It is a proper subset when not all outputs calculated.
                assert set(solution).issubset(expected_provides), (
                    f"Evictions left more data{list(iset(solution) - set(self.provides))} than {self}!"
                    ' \n Did you bypass "impossible-outputs" validation?'
                )

            return solution
        except Exception as ex:
            jetsam(ex, locals(), "solution")
            raise


class Network(Plottable):
    """
    A graph of operations that can :term:`compile` an execution plan.

    .. attribute:: needs

        the "base", all data-nodes that are not produced by some operation
    .. attribute:: provides

        the "base", all data-nodes produced by some operation
    """

    def __init__(self, *operations, graph=None):
        """

        :param operations:
            to be added in the graph
        :param graph:
            if None, create a new.

        :raises ValueError:
            if dupe operation, with msg:

                *Operations may only be added once, ...*
        """
        ## Check for duplicate, operations can only append  once.
        #
        uniques = set(operations)
        if len(operations) != len(uniques):
            dupes = list(operations)
            for i in uniques:
                dupes.remove(i)
            raise ValueError(f"Operations may only be added once, dupes: {list(dupes)}")

        if graph is None:
            # directed graph of operation and data nodes defining the net.
            graph = nx.DiGraph()
        else:
            if not isinstance(graph, nx.Graph):
                raise TypeError(f"Must be a NetworkX graph, was: {graph}")

        #: The :mod:`networkx` (Di)Graph containing all operations and dependencies,
        #: prior to :term:`compilation`.
        self.graph = graph

        for op in operations:
            self._append_operation(graph, op)
        self.needs, self.provides = collect_requirements(self.graph)

        #: Speed up :meth:`compile()` call and avoid a multithreading issue(?)
        #: that is occurring when accessing the dag in networkx.
        self._cached_plans = {}

    def __repr__(self):
        ops = list(yield_ops(self.graph.nodes))
        steps = (
            [f"\n  +--{s}" for s in self.graph.nodes]
            if is_debug()
            else ", ".join(n.name for n in ops)
        )
        return f"Network(x{len(self.graph.nodes)} nodes, x{len(ops)} ops: {''.join(steps)})"

    def find_ops(self, predicate) -> List[Operation]:
        """
        Scan operation nodes and fetch those satisfying `predicate`.

        :param predicate:
            the :term:`node predicate` is a 2-argument callable(op, node-data)
            that should return true for nodes to include.
        """
        return [
            n
            for n, d in self.graph.nodes.data(True)
            if isinstance(n, Operation) and predicate(n, d)
        ]

    def find_op_by_name(self, name) -> Union[Operation, None]:
        """Fetch the 1st operation named with the given `name`."""
        for n in yield_ops(self.graph.nodes):
            if n.name == name:
                return n

    def prepare_plot_args(self, plot_args: PlotArgs) -> PlotArgs:
        plot_args = plot_args.clone_or_merge_graph(self.graph)
        plot_args = plot_args.with_defaults(
            name=f"network-x{len(self.graph.nodes)}-nodes",
            inputs=self.needs,
            outputs=self.provides,
        )
        plot_args = plot_args._replace(plottable=self)

        return plot_args

    def _append_operation(self, graph, operation: Operation):
        """
        Adds the given operation and its data requirements to the network graph.

        - Invoked during constructor only (immutability).
        - Identities are based on the name of the operation, the names of the operation's needs,
          and the names of the data it provides.
        - Adds needs, operation & provides, in that order.

        :param graph:
            the `networkx` graph to append to
        :param operation:
            operation instance to append
        """
        ## Needs
        #
        needs = []
        needs_edges = []
        for n in getattr(operation, "op_needs", operation.needs):
            nkw, ekw = {}, {}
            if is_optional(n):
                ekw["optional"] = True
            if is_sideffect(n):
                ekw["sideffect"] = nkw["sideffect"] = True
            if is_mapped(n):
                ekw["fn_kwarg"] = n.fn_kwarg
            needs.append((n, nkw))
            needs_edges.append((n, operation, ekw))
        graph.add_nodes_from(needs)
        graph.add_node(operation, **operation.node_props)
        graph.add_edges_from(needs_edges)

        ## Prepare inversed-aliases index, used
        #  to label edges reaching to aliased `provides`.
        #
        aliases = getattr(operation, "aliases", None)
        alias_sources = {v: src for src, v in aliases} if aliases else ()

        ## Provides
        #
        for n in getattr(operation, "op_provides", operation.provides):
            kw = {}
            if is_sideffect(n):
                kw["sideffect"] = True
                graph.add_node(n, sideffect=True)

            if n in alias_sources:
                src_provide = alias_sources[n]
                kw["alias_of"] = src_provide

            graph.add_edge(operation, n, **kw)

    def _topo_sort_nodes(self, dag) -> List:
        """Topo-sort dag respecting operation-insertion order to break ties."""
        node_keys = dict(zip(dag.nodes, count()))
        return nx.lexicographical_topological_sort(dag, key=node_keys.get)

    def _apply_graph_predicate(self, graph, predicate):
        to_del = []
        for node, data in graph.nodes.items():
            try:
                if isinstance(node, Operation) and not predicate(node, data):
                    to_del.append(node)
            except Exception as ex:
                raise ValueError(
                    f"Node-predicate({predicate}) failed due to: {ex}\n  node: {node}, {self}"
                ) from ex
        log.info("... predicate filtered out %s.", [op.name for op in to_del])
        graph.remove_nodes_from(to_del)

    def _prune_graph(
        self, inputs: Items, outputs: Items, predicate: NodePredicate = None
    ) -> Tuple[nx.DiGraph, Collection, Collection, Collection]:
        """
        Determines what graph steps need to run to get to the requested
        outputs from the provided inputs:
        - Eliminate steps that are not on a path arriving to requested outputs;
        - Eliminate unsatisfied operations: partial inputs or no outputs needed;
        - consolidate the list of needs & provides.

        :param inputs:
            The names of all given inputs.
        :param outputs:
            The desired output names.  This can also be ``None``, in which
            case the necessary steps are all graph nodes that are reachable
            from the provided inputs.
        :param predicate:
            the :term:`node predicate` is a 2-argument callable(op, node-data)
            that should return true for nodes to include; if None, all nodes included.

        :return:
            a 3-tuple with the *pruned_dag* & the needs/provides resolved based
            on the given inputs/outputs
            (which might be a subset of all needs/outputs of the returned graph).

            Use the returned `needs/provides` to build a new plan.

        :raises ValueError:
            - if `outputs` asked do not exist in network, with msg:

                *Unknown output nodes: ...*
        """
        # TODO: break cycles here.
        dag = self.graph

        ##  When `inputs` is None, we have to keep all possible input nodes
        #   and this is achieved with 2 tricky locals:
        #
        #   inputs
        #       it is kept falsy, to disable the edge-breaking, so that
        #       the ascending_from_outputs that follows can reach all input nodes;
        #       including intermediate ones;
        #   satisfied_inputs
        #       it is filled with all possible input nodes, to trick `_unsatisfied_operations()`
        #       to assume their operations are satisfied, and keep them.
        #
        if inputs is None and outputs is None:
            satisfied_inputs, outputs = self.needs, self.provides
        else:
            if inputs is None:  # outputs: NOT None
                satisfied_inputs = self.needs - outputs
            else:  # inputs: NOT None, outputs: None
                # Just ignore `inputs` not in the graph.
                satisfied_inputs = inputs = iset(inputs) & dag.nodes

            ## Scream on unknown `outputs`.
            #
            if outputs:
                unknown_outputs = iset(outputs) - dag.nodes
                if unknown_outputs:
                    raise ValueError(
                        f"Unknown output nodes: {list(unknown_outputs)}\n  {self}"
                    )

        assert isinstance(satisfied_inputs, abc.Collection)
        assert inputs is None or isinstance(inputs, abc.Collection)
        assert outputs is None or isinstance(outputs, abc.Collection)

        broken_dag = dag.copy()  # preserve net's graph

        if predicate:
            self._apply_graph_predicate(broken_dag, predicate)

        # Break the incoming edges to all given inputs.
        #
        # Nodes producing any given intermediate inputs are unnecessary
        # (unless they are also used elsewhere).
        # To discover which ones to prune, we break their incoming edges
        # and they will drop out while collecting ancestors from the outputs.
        #
        if inputs:
            for n in inputs:
                # Coalesce to a list, to avoid concurrent modification.
                broken_dag.remove_edges_from(list(broken_dag.in_edges(n)))

        # Drop stray input values and operations (if any).
        if outputs is not None:
            # If caller requested specific outputs, we can prune any
            # unrelated nodes further up the dag.
            ending_in_outputs = set()
            for output_name in outputs:
                ending_in_outputs.add(output_name)
                ending_in_outputs.update(nx.ancestors(dag, output_name))
            broken_dag = broken_dag.subgraph(ending_in_outputs)
            if log.isEnabledFor(logging.INFO) and len(broken_dag) != len(dag):
                log.info(
                    "... dropping irrelevant ops%s.",
                    [
                        op.name
                        for op in dag
                        if isinstance(op, Operation) and op not in ending_in_outputs
                    ],
                )

        # Prune unsatisfied operations (those with partial inputs or no outputs).
        unsatisfied = _unsatisfied_operations(broken_dag, satisfied_inputs)
        if log.isEnabledFor(logging.INFO) and unsatisfied:
            log.info("... dropping unsatisfied ops%s.", [op.name for op in unsatisfied])
        # Clone it, to modify it.
        pruned_dag = dag.subgraph(broken_dag.nodes - unsatisfied).copy()
        # Clean unlinked data-nodes.
        pruned_dag.remove_nodes_from(list(nx.isolates(pruned_dag)))

        inputs = iset(
            _optionalized(pruned_dag, n) for n in satisfied_inputs if n in pruned_dag
        )
        if outputs is None:
            outputs = iset(
                n
                for n in self.provides
                if n not in inputs and n in pruned_dag and not is_sideffect(n)
            )
        else:
            # filter-out from new `provides` if pruned.
            outputs = iset(n for n in outputs if n in pruned_dag)

        assert inputs is not None or isinstance(inputs, abc.Collection)
        assert outputs is not None or isinstance(outputs, abc.Collection)

        return pruned_dag, tuple(inputs), tuple(outputs)

    def _build_execution_steps(
        self, pruned_dag, inputs: Collection, outputs: Optional[Collection]
    ) -> List:
        """
        Create the list of operation-nodes & *instructions* evaluating all

        operations & instructions needed a) to free memory and b) avoid
        overwriting given intermediate inputs.

        :param pruned_dag:
            The original dag, pruned; not broken.
        :param outputs:
            outp-names to decide whether to add (and which) evict-instructions

        Instances of :class:`_EvictInstructions` are inserted in `steps` between
        operation nodes to reduce the memory footprint of solutions while
        the computation is running.
        An evict-instruction is inserted whenever a *need* is not used
        by any other *operation* further down the DAG.
        """

        steps = []

        def add_step_once(step):
            # For functions with repeated needs, like ['a', 'a'].
            if steps and step == steps[-1] and type(step) == type(steps[-1]):
                log.warning("Skipped dupe step %s in position %i.", step, len(steps))
            else:
                steps.append(step)

        ## Create an execution order such that each layer's needs are provided,
        #  respecting operation-insertion order to break ties;  which means that
        #  the first inserted operations win the `needs`, but
        #  the last ones win the `provides` (and the final solution).
        ordered_nodes = iset(self._topo_sort_nodes(pruned_dag))

        # Add Operations evaluation steps, and instructions to evict data.
        for i, node in enumerate(ordered_nodes):

            if isinstance(node, Operation):
                steps.append(node)

                # NO EVICTIONS when no specific outputs asked.
                if not outputs or is_skip_evictions():
                    continue

                # Add EVICT (1) for operation's needs.
                #
                # Broken links are irrelevant bc they are predecessors of data (provides),
                # but here we scan for predecessors of the operation (needs).
                #
                for need in pruned_dag.pred[node]:
                    # Do not evict asked outputs or sideffects.
                    if need in outputs:
                        continue

                    # A needed-data of this operation may be evicted if
                    # no future Operations needs it.
                    #
                    for future_node in ordered_nodes[i + 1 :]:
                        if (
                            isinstance(future_node, Operation)
                            and need in pruned_dag.pred[future_node]
                        ):
                            break
                    else:
                        add_step_once(_EvictInstruction(need))

                # Add EVICT (2) for unused operation's provides.
                #
                # A provided-data is evicted if no future operation needs it
                # (and is not an asked output).
                # It MUST use the broken dag, not to evict data
                # that will be pinned(?), but to populate overwrites with them.
                #
                # .. image:: doc/source/images/unpruned_useless_provides.svg
                #
                for provide in node.provides:
                    # Do not evict asked outputs or sideffects.
                    if provide not in outputs and provide not in pruned_dag.nodes:
                        add_step_once(_EvictInstruction(provide))

            else:
                assert isinstance(
                    node, str
                ), f"Unrecognized network graph node {node}: {type(node).__name__!r}"

        return steps

    def compile(
        self, inputs: Items = None, outputs: Items = None, predicate=None
    ) -> ExecutionPlan:
        """
        Create or get from cache an execution-plan for the given inputs/outputs.

        See :meth:`_prune_graph()` and :meth:`_build_execution_steps()`
        for detailed description.

        :param inputs:
            A collection with the names of all the given inputs.
            If `None``, all inputs that lead to given `outputs` are assumed.
            If string, it is converted to a single-element collection.
        :param outputs:
            A collection or the name of the output name(s).
            If `None``, all reachable nodes from the given `inputs` are assumed.
            If string, it is converted to a single-element collection.
        :param predicate:
            the :term:`node predicate` is a 2-argument callable(op, node-data)
            that should return true for nodes to include; if None, all nodes included.

        :return:
            the cached or fresh new :term:`execution plan`

        :raises ValueError:
            - If `outputs` asked do not exist in network, with msg:

                *Unknown output nodes: ...*

            - If solution does not contain any operations, with msg:

                *Unsolvable graph: ...*

            - If given `inputs` mismatched plan's :attr:`needs`, with msg:

                *Plan needs more inputs...*

            - If net cannot produce asked `outputs`, with msg:

                *Unreachable outputs...*
        """
        ## Make a stable cache-key.
        #
        if inputs is not None:
            inputs = tuple(
                sorted(astuple(inputs, "inputs", allowed_types=abc.Collection))
            )
        if outputs is not None:
            outputs = tuple(
                sorted(astuple(outputs, "outputs", allowed_types=abc.Collection))
            )
        if not predicate:
            predicate = None

        cache_key = (inputs, outputs, predicate)

        ## Build (or retrieve from cache) execution plan
        #  for the given inputs & outputs.
        #
        if cache_key in self._cached_plans:
            log.debug("... cache-hit key: %s", cache_key)
            plan = self._cached_plans[cache_key]
        else:
            pruned_dag, needs, provides = self._prune_graph(inputs, outputs, predicate)
            steps = self._build_execution_steps(pruned_dag, needs, outputs or ())
            plan = ExecutionPlan(
                self,
                needs,
                provides,
                pruned_dag,
                tuple(steps),
                asked_outs=outputs is not None,
            )

            self._cached_plans[cache_key] = plan
            log.debug("... cache-updated key: %s", cache_key)

        return plan
