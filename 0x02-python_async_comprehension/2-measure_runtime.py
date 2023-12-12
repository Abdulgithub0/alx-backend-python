#!/usr/bin/env python3

"""Import async_comprehension from the previous file and write a measure_runtime
    coroutine that will execute async_comprehension four times in parallel using
    asyncio.gather.
    measure_runtime should measure the total runtime and return it.
"""

import asyncio
import time


async def measure_runtime():
    """collect and return a random numbers between 1 - 10 asyncronously"""
    async_com = __import__('1-async_comprehension').async_comprehension
    start_time = time.time()
    await asyncio.gather(async_com(), async_com(), async_com(), async_com())
    return time.time() - start_time
