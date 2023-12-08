#!/usr/bin/env python3
"""annotate the below function"""
from typing import Any, TypeVar, Union, Mapping

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """correct annotation"""
    if key in dct:
        return dct[key]
    else:
        return default
