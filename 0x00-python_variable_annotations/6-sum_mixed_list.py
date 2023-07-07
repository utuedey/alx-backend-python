#!/usr/bin/env python3

"""
6-sum_mixed_list module
Takes a list mxd_lst of integers and floats and returns their sum as a float.
"""
import typing

mxd = mxd_list = typing.List[typing.Union[int, float]]


def sum_mixed_list(mxd_list: mxd) -> float:
    """Return sum of the mixed list as a float"""
    return sum(mxd_list)
