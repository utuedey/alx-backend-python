#!/usr/bin/env python3

"""
7-to_kv module
Takes a string k and an int OR float v as arguments and returns a tuple.
"""
import typing


v_type = typing.Union[int, float]
r_type = typing.Tuple[str, float]


def to_kv(k: str, v: v_type) -> r_type:
    """Return a tuple of k and square of v."""
    return k, v**2
