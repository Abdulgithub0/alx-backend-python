#!/usr/bin/env python3

from asyncio import sleep
from random import import uniform

"""working with Asyncio module"""


async def wait_random(max_delay: int = 10) -> float:
    """wait for random sec then return the sec"""
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay


if __name__ == '__main__':
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
