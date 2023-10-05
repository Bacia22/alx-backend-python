#!/usr/bin/env python3
"""
Duck type and iteration
"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(1st: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
            """
            Args:
            1st: Sequence of list

            Return:
            List of tuple of sequence of integers
            """

            return [(i, len(1) for i in 1st]
