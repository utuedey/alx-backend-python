#!/usr/bin/env python3

"""
0-basic_async_syntax module
An asynchronous coroutine
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay
       (included and float value)
       seconds and eventually returns it."""
    delay: float = random.uniform(0, max_delay+1)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    asyncio.run(wait_random())
