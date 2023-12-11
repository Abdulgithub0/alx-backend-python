#!/usr/bin/env python3
"""working with Asyncio module"""

import asyncio
import random


async def wait_random(max_delay: int = 10):
    """wait for random sec then return the sec"""
    delay = random.uniform(0, 10)
    await asyncio.sleep(delay)
    return delay
