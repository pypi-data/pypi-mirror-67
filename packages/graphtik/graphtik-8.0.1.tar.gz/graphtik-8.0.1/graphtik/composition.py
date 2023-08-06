# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.
"""
.. default-role: term

`compose` `operation` & `dependency` into `pipeline`\\s match/zip inputs/outputs during `execution`.

.. default-role:
"""

import abc
import itertools as itt
import logging
import textwrap
from collections import abc as cabc
from functools import wraps
from typing import Any, Callable, Collection, List, Mapping, Tuple, Union

from boltons.setutils import IndexedSet as iset

from .base import (
    NO_RESULT,
    UNSET,
    Items,
    MultiValueError,
    PlotArgs,
    Plottable,
    aslist,
    astuple,
    func_name,
    jetsam,
)
from .config import (
    first_solid,
    is_debug,
    is_endure_operations,
    is_marshal_tasks,
    is_parallel_tasks,
    is_reschedule_operations,
    reset_abort,
)
from .modifiers import (
    dep_singularized,
    dep_stripped,
    is_mapped,
    is_optional,
    is_pure_sfx,
    is_sfx,
    is_sfxed,
    is_vararg,
    is_varargs,
    optional,
)

log = logging.getLogger(__name__)


def as_renames(i, argname):
    """
    Parses a list of (source-->destination) from dict, list-of-2-items, single 2-tuple.

    :return:
        a (possibly empty)list-of-pairs

    .. Note::
        The same `source` may be repeatedly renamed to multiple `destinations`.
    """
    if not i:
        return ()

    def is_list_of_2(i):
        try:
            return all(len(ii) == 2 for ii in i)
        except Exception:
            pass  # Let it be, it may be a dictionary...

    if isinstance(i, tuple) and len(i) == 2:
        i = [i]
    elif not isinstance(i, cabc.Collection):
        raise TypeError(
            f"Argument {argname} must be a list of 2-element items, was: {i!r}"
        ) from None
    elif not is_list_of_2(i):
        try:
            i = list(dict(i).items())
        except Exception as ex:
            raise ValueError(f"Cannot dict-ize {argname}({i!r}) due to: {ex}") from None

    return i


def reparse_operation_data(
    name, needs, provides
) -> Tuple[cabc.Hashable, cabc.Collection, cabc.Collection]:
    """
    Validate & reparse operation data as lists.

    :return:
        name, needs, provides,

    As a separate function to be reused by client building operations,
    to detect errors early.
    """

    if not isinstance(name, cabc.Hashable):
        raise TypeError(f"Operation `name` must be hashable, got: {name}")

    # Allow single string-value for needs parameter
    needs = astuple(needs, "needs", allowed_types=cabc.Collection)
    if not all(isinstance(i, str) for i in needs):
        raise TypeError(f"All `needs` must be str, got: {needs!r}")

    # Allow single value for provides parameter
    provides = astuple(provides, "provides", allowed_types=cabc.Collection)
    if not all(isinstance(i, str) for i in provides):
        raise TypeError(f"All `provides` must be str, got: {provides!r}")

    return name, needs, provides


class Operation(abc.ABC):
    """An abstract class representing an action with :meth:`.compute()`."""

    @property
    def __name__(self) -> str:
        return self.name  # pylint: disable=no-member

    @abc.abstractmethod
    def compute(self, named_inputs, outputs=None):
        """
        Compute (optional) asked `outputs` for the given `named_inputs`.

        It is called by :class:`.Network`.
        End-users should simply call the operation with `named_inputs` as kwargs.

        :param named_inputs:
            the input values with which to feed the computation.
        :returns list:
            Should return a list values representing
            the results of running the feed-forward computation on
            ``inputs``.
        """


def _spread_sideffects(
    deps: cabc.Collection,
) -> Tuple[cabc.Collection, cabc.Collection]:
    """
    Build fn/op dependencies from user ones by stripping or singularizing any :term:`sideffects`.

    :return:
        the given `deps` duplicated as ``(fn_deps,  op_deps)``, where any instances of
        :term:`sideffects` are processed like this:

        `fn_deps`
            - any :func:`.sfxed` are replaced by the :func:`stripped <.dep_stripped>`
              dependency consumed/produced by underlying functions, in the order
              they are first met (the rest duplicate `sideffected` are discarded).
            - any :func:`.sfx` are simply dropped;

        `op_deps`
            any :func:`.sfxed` are replaced by a sequence of ":func:`singularized
            <.dep_singularized>`" instances, one for each item in their
            :attr:`._Modifier.sfx_list` attribute, in the order they are first met
            (any duplicates are discarded, order is irrelevant, since they don't reach
            the function);
    """

    #: The dedupe  any `sideffected`.
    seen_sideffecteds = set()

    def strip_sideffecteds(dep):
        """Strip and dedupe any sfxed, drop any sfx. """
        if is_sfxed(dep):
            dep = dep_stripped(dep)
            if not dep in seen_sideffecteds:
                seen_sideffecteds.add(dep)
                return (dep,)
        elif not is_sfx(dep):
            return (dep,)
        return ()

    assert deps is not None

    if deps:
        deps = tuple(nn for n in deps for nn in dep_singularized(n))
        fn_deps = tuple(nn for n in deps for nn in strip_sideffecteds(n))
        return deps, fn_deps
    else:
        return deps, deps


class FunctionalOperation(Operation, Plottable):
    """
    An :term:`operation` performing a callable (ie a function, a method, a lambda).

    .. Tip::
        - Use :func:`.operation()` factory to build instances of this class instead.
        - Call :meth:`withset()` on existing instances to re-configure new clones.
    """

    def __init__(
        self,
        fn: Callable = None,
        name=None,
        needs: Items = None,
        provides: Items = None,
        aliases: Mapping = None,
        *,
        rescheduled=None,
        endured=None,
        parallel=None,
        marshalled=None,
        returns_dict=None,
        node_props: Mapping = None,
    ):
        """
        Build a new operation out of some function and its requirements.

        See :func:`.operation` for the full documentation of parameters,
        study the code for attributes (or read them from  rendered sphinx site).
        """
        super().__init__()
        node_props = node_props = node_props if node_props else {}

        if fn and not callable(fn):
            raise TypeError(f"Operation was not provided with a callable: {fn}")
        if node_props is not None and not isinstance(node_props, cabc.Mapping):
            raise TypeError(
                f"Operation `node_props` must be a dict, was {type(node_props).__name__!r}: {node_props}"
            )

        if name is None and fn:
            name = func_name(fn, None, mod=0, fqdn=0, human=0, partials=1)
        ## Overwrite reparsed op-data.
        name, needs, provides = reparse_operation_data(name, needs, provides)

        needs, _fn_needs = _spread_sideffects(needs)
        provides, _fn_provides = _spread_sideffects(provides)
        op_needs = iset(needs)

        if aliases:
            aliases = as_renames(aliases, "aliases")
            if any(1 for src, dst in aliases if dst in provides):
                bad = ", ".join(
                    f"{src} -> {dst}" for src, dst in aliases if dst in provides
                )
                raise ValueError(
                    f"The `aliases` ({bad}) clash with existing provides {list(provides)}!"
                )

            alias_src, alias_dst = list(zip(*aliases))
            if not set(alias_src) <= set(provides):
                raise ValueError(
                    f"The `aliases` for {list(alias_src)} rename {list(iset(alias_src) - provides)}"
                    f", not found in provides {list(provides)}!"
                )
            sfx_aliases = [
                f"{src} -> {dst}" for src, dst in aliases if is_sfx(src) or is_sfx(dst)
            ]
            if sfx_aliases:
                raise ValueError(
                    f"The `aliases` must not contain `sideffects` {sfx_aliases}"
                    "\n  Simply add any extra `sideffects` in the `provides`."
                )
        else:
            alias_dst = ()
        op_provides = iset(itt.chain(provides, alias_dst))

        #: The :term:`operation`'s underlying function.
        self.fn = fn
        #: a name for the operation (e.g. `'conv1'`, `'sum'`, etc..);
        #: any "parents split by dots(``.``)".
        #: :seealso: :ref:`operation-nesting`
        self.name = name

        #: The :term:`needs` almost as given by the user
        #: (which may contain MULTI-sideffecteds and dupes),
        #: roughly morphed into `_fn_provides` + sideffects
        #: (dupes preserved, with sideffects & SINGULARIZED :term:`sideffected`\s).
        #: It is stored for builder functionality to work.
        self.needs = needs
        #: Value names ready to lay the graph for :term:`pruning`
        #: (NO dupes, WITH aliases & sideffects, and SINGULAR :term:`sideffected`\s).
        self.op_needs = op_needs
        #: Value names the underlying function requires
        #: (dupes preserved, without sideffects, with stripped :term:`sideffected` dependencies).
        self._fn_needs = _fn_needs

        #: The :term:`provides` almost as given by the user
        #: (which may contain MULTI-sideffecteds and dupes),
        #: roughly morphed into `_fn_provides` + sideffects
        #: (dupes preserved, without aliases, with sideffects & SINGULARIZED :term:`sideffected`\s).
        #: It is stored for builder functionality to work.
        self.provides = provides
        #: Value names ready to lay the graph for :term:`pruning`
        #: (NO dupes, WITH aliases & sideffects, and SINGULAR sideffecteds).
        self.op_provides = op_provides
        #: Value names the underlying function produces
        #: (dupes preserved, without aliases & sideffects, with stripped :term:`sideffected` dependencies).
        self._fn_provides = _fn_provides
        #: an optional mapping of `fn_provides` to additional ones, together
        #: comprising this operations :term:`op_provides`.
        #:
        #: You cannot alias an :term:`alias`.
        self.aliases = aliases
        #: If true, underlying *callable* may produce a subset of `provides`,
        #: and the :term:`plan` must then :term:`reschedule` after the operation
        #: has executed.  In that case, it makes more sense for the *callable*
        #: to `returns_dict`.
        self.rescheduled = rescheduled
        #: If true, even if *callable* fails, solution will :term:`reschedule`;
        #: ignored if :term:`endurance` enabled globally.
        self.endured = endured
        #: execute in :term:`parallel`
        self.parallel = parallel
        #: If true, operation will be :term:`marshalled <marshalling>` while computed,
        #: along with its `inputs` & `outputs`.
        #: (usefull when run in `parallel` with a :term:`process pool`).
        self.marshalled = marshalled
        #: If true, it means the underlying function :term:`returns dictionary` ,
        #: and no further processing is done on its results,
        #: i.e. the returned output-values are not zipped with `provides`.
        #:
        #: It does not have to return any :term:`alias` `outputs`.
        #:
        #: Can be changed amidst execution by the operation's function,
        #: but it is easier for that function to simply call :meth:`.set_results_by_name()`.
        self.returns_dict = returns_dict
        #: Added as-is into NetworkX graph, and you may filter operations by
        #: :meth:`.NetworkOperation.withset()`.
        #: Also plot-rendering affected if they match `Graphviz` properties,
        #: unless they start with underscore(``_``).
        self.node_props = node_props

    def __eq__(self, other):
        """Operation identity is based on `name`."""
        return bool(self.name == getattr(other, "name", UNSET))

    def __hash__(self):
        """Operation identity is based on `name`."""
        return hash(self.name)

    def __repr__(self):
        """
        Display more informative names for the Operation class
        """
        needs = aslist(self.needs, "needs")
        provides = aslist(self.provides, "provides")
        aliases = aslist(self.aliases, "aliases")
        aliases = f", aliases={aliases!r}" if aliases else ""
        fn_name = self.fn and func_name(self.fn, None, mod=0, fqdn=0, human=0)
        nprops = f", x{len(self.node_props)}props" if self.node_props else ""
        resched = (
            "?" if first_solid(self.rescheduled, is_reschedule_operations()) else ""
        )
        endured = "!" if first_solid(self.endured, is_endure_operations()) else ""
        parallel = "|" if first_solid(self.parallel, is_parallel_tasks()) else ""
        marshalled = "&" if first_solid(self.marshalled, is_marshal_tasks()) else ""
        returns_dict_marker = self.returns_dict and "{}" or ""

        if is_debug():
            debug_needs = (
                f", op_needs={list(self.op_needs)}, fn_needs={list(self._fn_needs)}"
            )
            debug_provides = f", op_provides={list(self.op_provides)}, fn_provides={list(self._fn_provides)}"
        else:
            debug_needs = debug_provides = ""
        return (
            f"FunctionalOperation{endured}{resched}{parallel}{marshalled}(name={self.name!r}, "
            f"needs={needs!r}{debug_needs}, provides={provides!r}{debug_provides}{aliases}, "
            f"fn{returns_dict_marker}={fn_name!r}{nprops})"
        )

    @property
    def deps(self) -> Mapping[str, Collection]:
        """
        All :term:`dependency` names, including `op_` & internal `_fn_`.

        if not DEBUG, all deps are converted into lists, ready to be printed.
        """

        return {
            k: v if is_debug() else list(v)
            for k, v in zip(
                "needs op_needs fn_needs provides op_provides fn_provides".split(),
                (
                    self.needs,
                    self.op_needs,
                    self._fn_needs,
                    self.provides,
                    self.op_provides,
                    self._fn_provides,
                ),
            )
        }

    def withset(self, fn: Callable = None, **kw,) -> "FunctionalOperation":
        """Make a *clone* with the some values replaced. """
        ## Exclude calculated dep-fields.
        #
        me = {
            k: v
            for k, v in vars(self).items()
            if not k.startswith("_") and not k.startswith("op_")
        }
        if fn:
            me["fn"] = fn
        me.update(kw)
        return FunctionalOperation(**me)

    def _prepare_match_inputs_error(
        self,
        exceptions: List[Tuple[Any, Exception]],
        missing: List,
        varargs_bad: List,
        named_inputs: Mapping,
    ) -> ValueError:
        errors = [
            f"Need({n}) failed due to: {type(nex).__name__}({nex})"
            for n, nex in enumerate(exceptions, 1)
        ]
        ner = len(exceptions) + 1

        if missing:
            errors.append(f"{ner}. Missing compulsory needs{list(missing)}!")
            ner += 1
        if varargs_bad:
            errors.append(
                f"{ner}. Expected needs{list(varargs_bad)} to be non-str iterables!"
            )
        inputs = dict(named_inputs) if is_debug() else list(named_inputs)
        errors.append(f"+++inputs: {inputs}")
        errors.append(f"+++{self}")

        msg = textwrap.indent("\n".join(errors), " " * 4)
        raise MultiValueError(f"Failed preparing needs: \n{msg}", *exceptions)

    def _match_inputs_with_fn_needs(self, named_inputs) -> Tuple[list, list, dict]:
        positional, vararg_vals = [], []
        kwargs = {}
        errors, missing, varargs_bad = [], [], []
        for n in self._fn_needs:
            assert not is_sfx(n), locals()
            try:
                if n not in named_inputs:
                    if not is_optional(n) or is_sfx(n):
                        # It means `inputs` < compulsory `needs`.
                        # Compilation should have ensured all compulsories existed,
                        # but ..?
                        ##
                        missing.append(n)
                    continue

                ## TODO: augment modifiers with "retrievers" from `inputs`.
                inp_value = named_inputs[n]

                if is_mapped(n):
                    kwargs[n.fn_kwarg] = inp_value

                elif is_vararg(n):
                    vararg_vals.append(inp_value)

                elif is_varargs(n):
                    if isinstance(inp_value, str) or not isinstance(
                        inp_value, cabc.Iterable
                    ):
                        varargs_bad.append(n)
                    else:
                        vararg_vals.extend(i for i in inp_value)

                else:
                    positional.append(inp_value)

            except Exception as nex:
                log.debug(
                    "Cannot prepare op(%s) need(%s) due to: %s",
                    self.name,
                    n,
                    nex,
                    exc_info=nex,
                )
                errors.append((n, nex))

        if errors or missing or varargs_bad:
            raise self._prepare_match_inputs_error(
                errors, missing, varargs_bad, named_inputs
            )

        return positional, vararg_vals, kwargs

    def _zip_results_with_provides(self, results) -> dict:
        """Zip results with expected "real" (without sideffects) `provides`."""
        fn_expected: iset = self._fn_provides
        rescheduled = first_solid(is_reschedule_operations(), self.rescheduled)
        if self.returns_dict:

            if hasattr(results, "_asdict"):  # named tuple
                results = results._asdict()
            elif isinstance(results, cabc.Mapping):
                pass
            elif hasattr(results, "__dict__"):  # regular object
                results = vars(results)
            else:
                raise ValueError(
                    "Expected results as mapping, named_tuple, object, "
                    f"got {type(results).__name__!r}: {results}\n  {self}"
                )

            if rescheduled:
                fn_required = fn_expected
                # Canceled sfx are welcomed.
                fn_expected = iset(self.provides)
            else:
                fn_required = fn_expected

            res_names = results.keys()

            ## Allow unknown outs when dict,
            #  bc we can safely ignore them (and it's handy for reuse).
            #
            unknown = res_names - fn_expected
            if unknown:
                unknown = list(unknown)
                log.info(
                    "Results%s contained +%s unknown provides%s\n  %s",
                    list(res_names),
                    len(unknown),
                    list(unknown),
                    self,
                )

            missmatched = fn_required - res_names
            if missmatched:
                if rescheduled:
                    log.warning(
                        "... Op %r did not provide%s",
                        self.name,
                        list(fn_expected - res_names),
                    )
                else:
                    raise ValueError(
                        f"Got x{len(results)} results({list(results)}) mismatched "
                        f"-{len(missmatched)} provides({list(fn_expected)})!\n  {self}"
                    )

        elif results == NO_RESULT and rescheduled:
            # Cancel also any SFX.
            results = {p: False for p in set(self.provides) if is_sfx(p)}

        elif not fn_expected:  # All provides were sideffects?
            if results and results != NO_RESULT:
                ## Do not scream,
                #  it is common to call a function for its sideffects,
                # which happens to return an irrelevant value.
                log.warning(
                    "Ignoring result(%s) because no `provides` given!\n  %s",
                    results,
                    self,
                )
            results = {}

        else:  # Handle result sequence: no-result, single-item, many
            nexpected = len(fn_expected)

            if results == NO_RESULT:
                results = ()
                ngot = 0

            elif nexpected == 1:
                results = [results]
                ngot = 1

            else:
                # nexpected == 0 was method's 1st check.
                assert nexpected > 1, nexpected
                if isinstance(results, (str, bytes)) or not isinstance(
                    results, cabc.Iterable
                ):
                    raise TypeError(
                        f"Expected x{nexpected} ITERABLE results, "
                        f"got {type(results).__name__!r}: {results}\n  {self}"
                    )
                ngot = len(results)

            if ngot < nexpected and not rescheduled:
                raise ValueError(
                    f"Got {ngot - nexpected} fewer results, while expected x{nexpected} "
                    f"provides({list(fn_expected)})!\n  {self}"
                )

            if ngot > nexpected:
                ## Less problematic if not expecting anything but got something
                #  (e.g reusing some function for sideffects).
                extra_results_loglevel = (
                    logging.INFO if nexpected == 0 else logging.WARNING
                )
                logging.log(
                    extra_results_loglevel,
                    "Got +%s more results, while expected "
                    "x%s provides%s\n  results: %s\n  %s",
                    ngot - nexpected,
                    nexpected,
                    list(fn_expected),
                    results,
                    self,
                )

            results = dict(zip(fn_expected, results))  # , fillvalue=UNSET))

        assert isinstance(
            results, cabc.Mapping
        ), f"Abnormal results type {type(results).__name__!r}: {results}!"

        if self.aliases:
            alias_values = [
                (dst, results[src]) for src, dst in self.aliases if src in results
            ]
            results.update(alias_values)

        return results

    def compute(self, named_inputs=None, outputs: Items = None) -> dict:
        try:
            if self.fn is None:
                raise ValueError(
                    f"Operation was not yet provided with a callable `fn`!"
                )
            assert self.name is not None, self
            if named_inputs is None:
                named_inputs = {}

            positional, varargs, kwargs = self._match_inputs_with_fn_needs(named_inputs)
            results_fn = self.fn(*positional, *varargs, **kwargs)
            results_op = self._zip_results_with_provides(results_fn)

            outputs = astuple(outputs, "outputs", allowed_types=cabc.Collection)

            ## Keep only outputs asked.
            #  Note that plan's executors do not ask outputs
            #  (see `_OpTask.__call__`).
            #
            if outputs:
                outputs = set(n for n in outputs)
                results_op = {
                    key: val for key, val in results_op.items() if key in outputs
                }

            return results_op
        except Exception as ex:
            jetsam(
                ex,
                locals(),
                "outputs",
                "aliases",
                "results_fn",
                "results_op",
                operation="self",
                args=lambda locs: {
                    "positional": locs.get("positional"),
                    "varargs": locs.get("varargs"),
                    "kwargs": locs.get("kwargs"),
                },
            )
            raise

    def __call__(self, *args, **kwargs):
        """Like dict args, delegates to :meth:`.compute()`."""
        return self.compute(dict(*args, **kwargs))

    def prepare_plot_args(self, plot_args: PlotArgs) -> PlotArgs:
        """Delegate to a provisional network with a single op . """
        from .plot import graphviz_html_string

        is_user_label = bool(plot_args.graph and plot_args.graph.get("graphviz.label"))
        plottable = compose(self.name, self)
        plot_args = plot_args.with_defaults(name=self.name)
        plot_args = plottable.prepare_plot_args(plot_args)
        assert plot_args.graph, plot_args

        ## Operations don't need another name visible.
        #
        if is_user_label:
            del plot_args.graph.graph["graphviz.label"]
        plot_args = plot_args._replace(plottable=self)

        return plot_args


def operation(
    fn: Callable = None,
    name=None,
    needs: Items = None,
    provides: Items = None,
    aliases: Mapping = None,
    *,
    rescheduled=None,
    endured=None,
    parallel=None,
    marshalled=None,
    returns_dict=None,
    node_props: Mapping = None,
):
    r"""
    An :term:`operation` factory that can function as a decorator.

    :param fn:
        The callable underlying this operation.
        If given, it builds the operation right away (along with any other arguments).

        If not given, it returns a "fancy decorator" that still supports all arguments
        here AND the ``withset()`` method.

        .. hint::
            This is a twisted way for `"fancy decorators"
            <https://realpython.com/primer-on-python-decorators/#both-please-but-never-mind-the-bread>`_.

        After all that, you can always call :meth:`FunctionalOperation.withset()`
        on existing operation, to obtain a re-configured clone.
    :param str name:
        The name of the operation in the computation graph.
        If not given, deduce from any `fn` given.

    :param needs:
        the list of (positionally ordered) names of the data needed by the `operation`
        to receive as :term:`inputs`, roughly corresponding to the arguments of
        the underlying `fn` (plus any :term:`sideffects`).

        It can be a single string, in which case a 1-element iterable is assumed.

        .. seealso::
            - :term:`needs`
            - :term:`modifier`
            - :attr:`.FunctionalOperation.needs`
            - :attr:`.FunctionalOperation.op_needs`
            - :attr:`.FunctionalOperation._fn_needs`


    :param provides:
        the list of (positionally ordered) output data this operation provides,
        which must, roughly, correspond to the returned values of the `fn`
        (plus any :term:`sideffects` & :term:`alias`\es).

        It can be a single string, in which case a 1-element iterable is assumed.

        If they are more than one, the underlying function must return an iterable
        with same number of elements, unless param `returns_dict` :term:`is true
        <returns dictionary>`, in which case must return a dictionary that containing
        (at least) those named elements.

        .. seealso::
            - :term:`provides`
            - :term:`modifier`
            - :attr:`.FunctionalOperation.provides`
            - :attr:`.FunctionalOperation.op_provides`
            - :attr:`.FunctionalOperation._fn_provides`

    :param aliases:
        an optional mapping of `provides` to additional ones
    :param rescheduled:
        If true, underlying *callable* may produce a subset of `provides`,
        and the :term:`plan` must then :term:`reschedule` after the operation
        has executed.  In that case, it makes more sense for the *callable*
        to `returns_dict`.
    :param endured:
        If true, even if *callable* fails, solution will :term:`reschedule`.
        ignored if :term:`endurance` enabled globally.
    :param parallel:
        execute in :term:`parallel`
    :param marshalled:
        If true, operation will be :term:`marshalled <marshalling>` while computed,        along with its `inputs` & `outputs`.
        (usefull when run in `parallel` with a :term:`process pool`).
    :param returns_dict:
        if true, it means the `fn` :term:`returns dictionary` with all `provides`,
        and no further processing is done on them
        (i.e. the returned output-values are not zipped with `provides`)
    :param node_props:
        Added as-is into NetworkX graph, and you may filter operations by
        :meth:`.NetworkOperation.withset()`.
        Also plot-rendering affected if they match `Graphviz` properties.,
        unless they start with underscore(``_``)

    :return:
        when called with `fn`, it returns a :class:`.FunctionalOperation`,
        otherwise it returns a decorator function that accepts `fn` as the 1st argument.

        .. Note::
            Actually the returned decorator is the :meth:`.FunctionalOperation.withset()`
            method and accepts all arguments, monkeypatched to support calling a virtual
            ``withset()`` method on it, not to interrupt the builder-pattern,
            but only that - besides that trick, it is just a bound method.

    **Example:**

    This is an example of its use, based on the "builder pattern":

        >>> from graphtik import operation, varargs

        >>> op = operation()
        >>> op
        <function FunctionalOperation.withset at ...

    That's a "fancy decorator".

        >>> op = op.withset(needs=['a', 'b'])
        >>> op
        FunctionalOperation(name=None, needs=['a', 'b'], provides=[], fn=None)

    If you call an operation with `fn` un-initialized, it will scream:

        >>> op.compute({"a":1, "b": 2})
        Traceback (most recent call last):
        ValueError: Operation was not yet provided with a callable `fn`!

    You may keep calling ``withset()`` until a valid operation instance is returned,
    and compute it:

        >>> op = op.withset(needs=['a', 'b'],
        ...                 provides='SUM', fn=lambda a, b: a + b)
        >>> op
        FunctionalOperation(name='<lambda>', needs=['a', 'b'], provides=['SUM'], fn='<lambda>')
        >>> op.compute({"a":1, "b": 2})
        {'SUM': 3}

        >>> op.withset(fn=lambda a, b: a * b).compute({'a': 2, 'b': 5})
        {'SUM': 10}
    """
    kw = {k: v for k, v in locals().items() if v is not None and k != "self"}
    op = FunctionalOperation(**kw)

    if "fn" in kw:
        # Either used as a "naked" decorator (without any arguments)
        # or not used as decorator at all (manually called and passed in `fn`) .
        return op

    @wraps(op.withset)
    def decorator(*args, **kw):
        return op.withset(*args, **kw)

    # Dress decorator to support the builder-pattern.
    # even when called as regular function (without `@`) without `fn`.
    decorator.withset = op.withset

    return decorator


class NULL_OP(FunctionalOperation):
    """
    Eliminates same-named operations added later during term:`operation merging`.

    :seealso: :ref:`operation-merging`
    """

    def __init__(self, name):
        super().__init__(name=name)

    def compute(self, *args, **kw):
        raise AssertionError("Should have been eliminated!")


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
