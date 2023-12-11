#!/usr/bin/env python3

import asyncio
import random

"""working with Asyncio module"""


async def wait_random(max_delay: int = 10) -> float:
    """wait for random sec then return the sec"""
    delay = random(0, max_delay)
    await asyncio.sleep(delay)
    return delay
