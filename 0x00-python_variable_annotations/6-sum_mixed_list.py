#!/usr/bin/env python3
"""
Mixed lists
"""
from typing import Union, List


def sum_mixed_list(mxd_1st: List[Union[int, float]]) -> float
"""
Args:
    mxd_1st: float-int numbers

    Return:
    Float base in int or float numbers
    """

    result: float = 0

    for x in mxd_1st:
        result += x

        return result
