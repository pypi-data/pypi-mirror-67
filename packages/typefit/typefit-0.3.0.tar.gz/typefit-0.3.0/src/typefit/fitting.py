from collections import abc
from enum import Enum
from inspect import isclass
from typing import Any, Optional, Type, Union

from .compat import get_args, get_origin
from .nodes import *
from .reporting import ErrorReporter, LogErrorReporter, PrettyJson5Formatter


class Fitter:
    """
    Core class responsible for the fitting of objects.

    - Create an instance with the configuration you want
    - Use the :py:meth:`~.fit` method to do your fittings

    Notes
    -----
    Overall orchestrator of the fitting. A lot of the logic happens in the
    nodes, but this class is responsible for executing the logic in the right
    order and also holds configuration.
    """

    def __init__(
        self,
        no_unwanted_keys: bool = False,
        error_reporter: Optional[ErrorReporter] = None,
    ):
        """
        Constructs the instance.

        Parameters
        ----------
        no_unwanted_keys
            If set to ``True``, it will not be allowed to have unwanted keys
            when fitting mappings into dataclasses/named tuples.
        error_reporter
            Error reporting for when a validation fails. By default no report
            is made but you might want to arrange reporting for your needs,
            otherwise you're going to be debugging in the blind.
        """

        self.no_unwanted_keys = no_unwanted_keys
        self.error_reporter = error_reporter

    def _as_node(self, value: Any):
        """
        Recursively transforms a value into a node.

        Parameters
        ----------
        value
            Any kind of JSON-decoded value (string, list, object, etc).
        """

        if isinstance(value, (int, float, str, bool)) or value is None:
            return FlatNode(self, value)
        elif isinstance(value, abc.Sequence):
            return ListNode(self, value, [self._as_node(x) for x in value])
        elif isinstance(value, abc.Mapping):
            return MappingNode(
                self, value, {k: self._as_node(v) for k, v in value.items()}
            )
        else:
            raise ValueError

    def _fit_union(self, t: Type[T], value: Node) -> T:
        """
        In case of a union, walk through all possible types and try them on
        until one fits (fails otherwise).
        """

        for sub_t in get_args(t):
            try:
                return self.fit_node(sub_t, value)
            except ValueError:
                continue

        value.fail("No matching type in Union")

    def _fit_class(self, t: Type[T], value: Node) -> T:
        """
        Wrapper around the ``FlatNode``'s fit method.
        """

        if isinstance(value, FlatNode):
            return value.fit(t)

        value.fail(f"Node is not {t}")

    def _fit_any(self, _: Type[T], value: Node) -> T:
        """
        That's here for consistency but let's be honest, this function is not
        very useful.
        """

        return value.value

    def _fit_none(self, _: Type[T], value: Node) -> T:
        """
        Does basic checks before returning None or raising an error
        """

        if value.value is None:
            value.fit_success = True
            return None

        value.fail(f"Value is not None")

    def _fit_enum(self, t: Type[T], value: Node) -> T:
        """
        Tries to find back the right enum value
        """

        try:
            out = t(value.value)
        except ValueError:
            value.fail(f"No match in enum {t!r}")
        else:
            value.fit_success = True
            return out

    def fit_node(self, t: Type[T], value: Node) -> T:
        """
        Tries to find the right fit according to the type you're trying to
        match and the node type.

        Notes
        -----
        The order of tests done in this code is very important. By example,
        dataclasses would pass the ``isclass(t)`` test so ``MappingNode`` have
        to be handled before that test.

        Parameters
        ----------
        t
            Type you want to fit your node into
        value
            A node you want to fit into a type

        Raises
        ------
        ValueError
        """

        if get_origin(t) is Union:
            return self._fit_union(t, value)
        elif t is Any:
            return self._fit_any(t, value)
        elif isinstance(value, (MappingNode, ListNode)):
            return value.fit(t)
        elif t is None or t is None.__class__:
            return self._fit_none(t, value)
        elif isclass(t):
            if issubclass(t, Enum):
                return self._fit_enum(t, value)
            else:
                return self._fit_class(t, value)
        else:
            value.fail("Could not fit. This error can never be reached in theory.")

    def fit(self, t: Type[T], value: Any) -> T:
        """
        Fits data into a type. The data is expected to be JSON-decoded values
        (strings, ints, bools, etc).

        On failure a ValueError will arise and if an error reporter is set it
        will be sent the node to generate the error report.

        Parameters
        ----------
        t
            Type you want to fit the value into
        value
            Value you want to fit into a type

        Raises
        -------
        ValueError
        """

        node = self._as_node(value)

        try:
            return self.fit_node(t, node)
        except ValueError:
            if self.error_reporter:
                self.error_reporter.report(node)
            raise


def typefit(t: Type[T], value: Any) -> T:
    """
    Fits a JSON-decoded value into native Python type-annotated objects.

    This uses the default sane settings but it might not be up to your taste.
    By example, errors will be reported in the logging module using ANSI escape
    codes for syntactical coloration, however depending on the situation you
    might not want that.

    If you want more flexibility and configuration, you can use the
    :py:class:`~.Fitter` directly.

    Parameters
    ----------
    t
        Type to fit the value into. Currently supported types are:

          - Simple builtins like :class:`int`, :class:`float`,
            :class:`typing.Text`, :class:`typing.bool`
          - Enumerations which are subclass of :class:`enum.Enum`.
          - Custom types. The constructor needs to accept exactly one parameter
            and that parameter should have a typing annotation.
          - :class:`typing.Union` to define several possible types
          - :class:`typing.List` to declare a list and the type of list values
    value
        Value to be fit into the type

    Returns
    -------
    T
        If the value fits, a value of the right type is returned.

    Raises
    ------
    ValueError
        When the fitting cannot be done, a :class:`ValueError` is raised.

    See Also
    --------
    Fitter.fit
    """

    return Fitter(
        error_reporter=LogErrorReporter(
            formatter=PrettyJson5Formatter(colors="terminal16m")
        )
    ).fit(t, value)
