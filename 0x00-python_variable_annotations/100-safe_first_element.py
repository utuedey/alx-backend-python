#!/usr/bin/env python3

"""
100-safe_first_element module.
"""

from typing import Any, Sequence, Union


r_type = Union[Any, None]
arg_type = Sequence[Any]


def safe_first_element(lst: arg_type) -> r_type:
    """Retrieves the first element of a sequence if it exists.
    """
    if lst:
        return lst[0]
    else:
        return None
