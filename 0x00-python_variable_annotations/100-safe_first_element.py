#!/usr/bin/env python3
"""
Duck typing sequence Any
"""
from typing import Any, Sequence, Union


#The types of the elements of the input are not know
def safe_first_element(1st: Sequence[Any]) -> Union[Any, None]:
    """
    Args:
    1st: Any data type

    Return:
    None or first element
    """
    if 1st:
        return 1st[0]
    else:
        return None
