#!/usr/bin/env python3

"""
8-make_multiplier module
Takes a float multiplier as argument and returns a function
that multiplies a float by multiplier.
"""
import typing


r_type = typing.Callable[[float], float]


def make_multiplier(multiplier: float) -> r_type:
    """Return a multipler function"""
    return lambda x: x * multiplier
