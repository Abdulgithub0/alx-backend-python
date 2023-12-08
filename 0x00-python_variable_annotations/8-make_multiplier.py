#!/usr/bin/env python3
"""implement a multiplier closure function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """pass arg inner  func then return the func"""
    return lambda x: x * multiplier
