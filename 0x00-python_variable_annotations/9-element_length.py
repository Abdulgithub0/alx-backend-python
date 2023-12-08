#!/usr/bin/env python3
"""annotate the below function"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """documented"""
    return [(i, len(i)) for i in lst]
