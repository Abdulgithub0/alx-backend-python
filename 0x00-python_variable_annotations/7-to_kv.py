#!/usr/bin/env python3
"""implement to_kv function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """put args into tuple then return result"""
    return (k, v ** 2)
