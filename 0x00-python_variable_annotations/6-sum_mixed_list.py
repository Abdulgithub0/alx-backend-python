#!/usr/bin/env python3
"""implement sum_list function"""

from typing import List, Union


def sum_mixed_list(input_float: List[Union[int, float]]) -> float:
    """add all the ele of the list then return result"""
    return sum(input_float)
