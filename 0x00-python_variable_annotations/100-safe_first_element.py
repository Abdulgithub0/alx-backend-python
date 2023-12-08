#!/usr/bin/env python3
"""annotate the below function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """correct duck type"""
    if lst:
        return lst[0]
    else:
        return None
