# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.
""":term:`composition` and :term:`operation merging` into :term:`pipeline`\\s. """

import logging
import re
from collections import abc
from typing import Any, Callable, Collection, List, Mapping, Union

from .base import UNSET, Items, PlotArgs, Plottable, aslist, astuple, jetsam
from .config import is_debug, reset_abort
from .modifiers import optional
from .op import NULL_OP, FunctionalOperation, Operation, reparse_operation_data

log = logging.getLogger(__name__)


def _id_bool(b):
    return hash(bool(b)) + 1


def _id_tristate_bool(b):
    return 3 if b is None else (hash(bool(b)) + 1)


class NetworkOperation(Operation, Plottable):
    """
    An operation that can :term:`compute` a network-graph of operations.

    .. Tip::
        Use :func:`compose()` factory to prepare the `net` and build
        instances of this class.
    """

    #: The name for the new netop, used when nesting them.
    name = None
    #: Will prune `net` against these possible outputs when :meth:`compute()` called.
    outputs = None
    #: The :term:`node predicate` is a 2-argument callable(op, node-data)
    #: that should return true for nodes to include; if None, all nodes included.
    predicate = None
    #: The execution_plan of the last call to compute(), stored as debugging aid.
    last_plan = None
    #: The outputs names (possibly `None`) used to compile the :attr:`plan`.
    outputs = None

    def __init__(
        self,
        operations,
        name,
        *,
        outputs=None,
        predicate: "NodePredicate" = None,
        rescheduled=None,
        endured=None,
        parallel=None,
        marshalled=None,
        nest=None,
        node_props=None,
    ):
        """
        For arguments, ee :meth:`withset()` & class attributes.

        :raises ValueError:
            if dupe operation, with msg:

                *Operations may only be added once, ...*
        """
        from .network import build_network

        ## Set data asap, for debugging, although `net.withset()` will reset them.
        self.name = name
        # Remember Outputs for future `compute()`?
        self.outputs = outputs
        self.predicate = predicate

        # Prune network
        self.net = build_network(
            operations, rescheduled, endured, parallel, marshalled, nest, node_props
        )
        self.name, self.needs, self.provides = reparse_operation_data(
            self.name, self.net.needs, self.net.provides
        )

    def __repr__(self):
        """
        Display more informative names for the Operation class
        """
        from .network import yield_ops

        clsname = type(self).__name__
        needs = aslist(self.needs, "needs")
        provides = aslist(self.provides, "provides")
        ops = list(yield_ops(self.net.graph))
        steps = (
            "".join(f"\n  +--{s}" for s in ops)
            if is_debug()
            else ", ".join(str(s.name) for s in ops)
        )
        return f"{clsname}({self.name!r}, needs={needs}, provides={provides}, x{len(ops)} ops: {steps})"

    @property
    def ops(self) -> List[Operation]:
        """A new list with all :term:`operation`\\s contained in the :term:`network`."""
        from .network import yield_ops

        return list(yield_ops(self.net.graph))

    def withset(
        self,
        outputs: Items = UNSET,
        predicate: "NodePredicate" = UNSET,
        *,
        name=None,
        rescheduled=None,
        endured=None,
        parallel=None,
        marshalled=None,
    ) -> "NetworkOperation":
        """
        Return a copy with a network pruned for the given `needs` & `provides`.

        :param outputs:
            Will be stored and applied on the next :meth:`compute()` or :meth:`compile()`.
            If not given, the value of this instance is conveyed to the clone.
        :param predicate:
            Will be stored and applied on the next :meth:`compute()` or :meth:`compile()`.
            If not given, the value of this instance is conveyed to the clone.
        :param name:
            the name for the new netop:

            - if `None`, the same name is kept;
            - if True, a distinct name is  devised::

                <old-name>-<uid>

            - otherwise, the given `name` is applied.
        :param rescheduled:
            applies :term:`reschedule`\\d to all contained `operations`
        :param endured:
            applies :term:`endurance` to all contained `operations`
        :param parallel:
            mark all contained `operations` to be executed in :term:`parallel`
        :param marshalled:
            mark all contained `operations` to be :term:`marshalled <marshalling>`
            (usefull when run in `parallel` with a :term:`process pool`).

        :return:
            A narrowed netop clone, which **MIGHT be empty!***

        :raises ValueError:
            - If `outputs` asked do not exist in network, with msg:

                *Unknown output nodes: ...*

        """
        from .network import yield_ops

        outputs = self.outputs if outputs == UNSET else outputs
        predicate = self.predicate if predicate == UNSET else predicate

        if name is None:
            name = self.name
        elif name is True:
            name = self.name

            ## Devise a stable UID based args.
            #
            uid = str(
                abs(
                    hash(str(outputs))
                    ^ hash(predicate)
                    ^ (1 * _id_bool(rescheduled))
                    ^ (2 * _id_bool(endured))
                    ^ (4 * _id_tristate_bool(parallel))
                    ^ (8 * _id_tristate_bool(marshalled))
                )
            )[:7]
            m = re.match(r"^(.*)-(\d+)$", name)
            if m:
                name = m.group(1)
            name = f"{name}-{uid}"

        return NetworkOperation(
            list(yield_ops(self.net.graph)),
            name,
            outputs=outputs,
            predicate=predicate,
            rescheduled=rescheduled,
            endured=endured,
            parallel=parallel,
            marshalled=marshalled,
        )

    def prepare_plot_args(self, plot_args: PlotArgs) -> PlotArgs:
        """Delegate to network if last-plan does not exist. """
        from .plot import graphviz_html_string

        plottable = self.last_plan or self.net
        plot_args = plot_args.with_defaults(name=self.name)
        plot_args = plottable.prepare_plot_args(plot_args)
        assert plot_args.graph, plot_args

        plot_args.graph.graph.setdefault(
            "graphviz.label", graphviz_html_string(self.name)
        )
        plot_args = plot_args._replace(plottable=self)

        return plot_args

    def compile(
        self, inputs=None, outputs=UNSET, predicate: "NodePredicate" = UNSET
    ) -> "ExecutionPlan":
        """
        Produce a :term:`plan` for the given args or `outputs`/`predicate` narrowed earlier.

        :param named_inputs:
            a string or a list of strings that should be fed to the `needs` of all operations.
        :param outputs:
            A string or a list of strings with all data asked to compute.
            If ``None``, all possible intermediate outputs will be kept.
            If not given, those set by a previous call to :meth:`withset()` or cstor are used.
        :param predicate:
            Will be stored and applied on the next :meth:`compute()` or :meth:`compile()`.
            If not given, those set by a previous call to :meth:`withset()` or cstor are used.

        :return:
            the :term:`execution plan` satisfying the given `inputs`, `outputs` & `predicate`

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
        outputs = self.outputs if outputs == UNSET else outputs
        predicate = self.predicate if predicate == UNSET else predicate

        return self.net.compile(inputs, outputs, predicate)

    def compute(
        self,
        named_inputs: Mapping = UNSET,
        outputs: Items = UNSET,
        predicate: "NodePredicate" = UNSET,
    ) -> "Solution":
        """
        Compile a plan & :term:`execute` the graph, sequentially or parallel.

        .. Attention::
            If intermediate :term:`compilation` is successful, the "global
            :term:`abort run` flag is reset before the :term:`execution` starts.

        :param named_inputs:
            A mapping of names --> values that will be fed to the `needs` of all operations.
            Cloned, not modified.
        :param outputs:
            A string or a list of strings with all data asked to compute.
            If ``None``, all intermediate data will be kept.

        :return:
            The :term:`solution` which contains the results of each operation executed
            +1 for inputs in separate dictionaries.

        :raises ValueError:
            - If `outputs` asked do not exist in network, with msg:

                *Unknown output nodes: ...*

            - If plan does not contain any operations, with msg:

                *Unsolvable graph: ...*

            - If given `inputs` mismatched plan's :attr:`needs`, with msg:

                *Plan needs more inputs...*

            - If net cannot produce asked `outputs`, with msg:

                *Unreachable outputs...*

        See also :meth:`.Operation.compute()`.
        """
        try:
            if named_inputs is UNSET:
                named_inputs = {}

            net = self.net  # jetsam
            outputs = self.outputs if outputs == UNSET else outputs
            predicate = self.predicate if predicate == UNSET else predicate

            # Build the execution plan.
            log.debug("=== Compiling netop(%s)...", self.name)
            self.last_plan = plan = net.compile(named_inputs.keys(), outputs, predicate)

            # Restore `abort` flag for next run.
            reset_abort()

            solution = plan.execute(named_inputs, outputs, name=self.name)

            return solution
        except Exception as ex:
            jetsam(ex, locals(), "plan", "solution", "outputs", network="net")
            raise

    def __call__(self, **input_kwargs) -> "Solution":
        """
        Delegates to :meth:`compute()`, respecting any narrowed `outputs`.
        """
        # To respect narrowed `outputs` must send them due to recompilation.
        return self.compute(input_kwargs, outputs=self.outputs)


def compose(
    name,
    op1,
    *operations,
    outputs: Items = None,
    rescheduled=None,
    endured=None,
    parallel=None,
    marshalled=None,
    nest: Union[Callable[["NestArgs"], str], Union[bool, str]] = None,
    node_props=None,
) -> NetworkOperation:
    """
    Composes a collection of operations into a single computation graph,
    obeying the ``nest`` property, if set in the constructor.

    Operations given earlier (further to the left) override those following
    (further to the right), similar to `set` behavior (and contrary to `dict`).

    :param str name:
        A optional name for the graph being composed by this object.
    :param op1:
        syntactically force at least 1 operation
    :param operations:
        Each argument should be an operation instance created using
        ``operation``.
    :param nest:
        - If false (default), applies :term:`operation merging`, not *nesting*.
        - if true, applies :term:`operation nesting` to :all types of nodes
          (performed by :func:`.nest_any_node()`;
        - if it is a :func:`.callable`, it is given a :class:`.NestArgs` instance
          to decide the node's name.

          The callable may return a *str* for the new-name, or any other true/false
          to apply default nesting which is to rename all nodes, as performed
          by :func:`.nest_any_node()`.

          For example, to nest just operation's names (but not their dependencies),
          call::

              compose(
                  ...,
                  nest=lambda nest_args: nest_args.typ == "op"
              )

          .. Attention::
              The callable SHOULD wish to preserve any :term:`modifier` on dependencies,
              and use :func:`.dep_renamed`.

          :seealso: :ref:`operation-nesting` for examples

    :param rescheduled:
        applies :term:`reschedule`\\d to all contained `operations`
    :param endured:
        applies :term:`endurance` to all contained `operations`
    :param parallel:
        mark all contained `operations` to be executed in :term:`parallel`
    :param marshalled:
        mark all contained `operations` to be :term:`marshalled <marshalling>`
        (usefull when run in `parallel` with a :term:`process pool`).
    :param node_props:
        Added as-is into NetworkX graph, to provide for filtering
        by :meth:`.NetworkOperation.withset()`.
        Also plot-rendering affected if they match `Graphviz` properties,
        unless they start with underscore(``_``)

    :return:
        Returns a special type of operation class, which represents an
        entire computation graph as a single operation.

    :raises ValueError:
        If the `net`` cannot produce the asked `outputs` from the given `inputs`.
    """
    operations = (op1,) + operations
    if not all(isinstance(op, Operation) for op in operations):
        raise TypeError(f"Non-Operation instances given: {operations}")
    return NetworkOperation(
        operations,
        name,
        outputs=outputs,
        rescheduled=rescheduled,
        endured=endured,
        parallel=parallel,
        marshalled=marshalled,
        nest=nest,
        node_props=node_props,
    )
