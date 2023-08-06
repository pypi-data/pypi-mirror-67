"""
Compatibility module that backports the get_origin and get_args functions from
Python 3. This code is from the official standard library.

Copyright © 2001-2019 Python Software Foundation; All Rights Reserved
"""

import collections

# noinspection PyUnresolvedReferences,PyProtectedMember
from typing import Any, Generic, Tuple, _GenericAlias

try:
    from typing import get_origin
except ImportError:

    def get_origin(tp) -> Any:
        """Get the unsubscripted version of a type.

        This supports generic types, Callable, Tuple, Union, Literal, Final and ClassVar.
        Return None for unsupported types. Examples::

            get_origin(Literal[42]) is Literal
            get_origin(int) is None
            get_origin(ClassVar[int]) is ClassVar
            get_origin(Generic) is Generic
            get_origin(Generic[T]) is Generic
            get_origin(Union[T, int]) is Union
            get_origin(List[Tuple[T, T]][int]) == list
        """
        if isinstance(tp, _GenericAlias):
            return tp.__origin__
        if tp is Generic:
            return Generic
        return None


try:
    from typing import get_args  # lgtm[py/unused-import]
except ImportError:

    def get_args(tp) -> Tuple[Any, ...]:
        """Get type arguments with all substitutions performed.

        For unions, basic simplifications used by Union constructor are performed.
        Examples::
            get_args(Dict[str, int]) == (str, int)
            get_args(int) == ()
            get_args(Union[int, Union[T, int], str][int]) == (int, str)
            get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
            get_args(Callable[[], T][int]) == ([], int)
        """
        if isinstance(tp, _GenericAlias):
            res = tp.__args__
            if get_origin(tp) is collections.abc.Callable and res[0] is not Ellipsis:
                res = (list(res[:-1]), res[-1])
            return res
        return ()
