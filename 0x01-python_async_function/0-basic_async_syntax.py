#!/usr/bin/env python3


from asyncio import sleep
from random import import uniform


"""Write an asynchronous coroutine that takes in an integer argument
   (max_delay, with a default value of 10) named wait_random that waits
   for a random delay between 0 and max_delay (included and float value)
   seconds and eventually returns it.
"""


async def wait_random(max_delay: int = 10) -> float:
    """wait for random second then return the second"""
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
