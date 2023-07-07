#!/usr/bin/env python3

"""
6-sum_mixed_list module
Takes a list mxd_lst of integers and floats and returns their sum as a float.
"""
import typing

mxd_list = typing.Union[int, float]
def sum_mixed_list(mxd_list) -> float:
    return sum(mxd_list)
