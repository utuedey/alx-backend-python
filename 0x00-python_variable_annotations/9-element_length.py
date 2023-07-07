#!/usr/bin/env python3

"""
9-element_length module
Annotate function’s parameters and return values with the appropriate types
"""
import typing


arg_type = typing.Iterable[typing.Sequence]
r_type = typing.List[typing.Tuple[typing.Sequence, int]]


def element_length(lst: arg_type) -> r_type:
    """Return values with appropriatet types"""
    return [(i, len(i)) for i in lst]
