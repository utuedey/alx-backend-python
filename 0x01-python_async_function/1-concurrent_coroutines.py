#!/usr/bin/env python3

"""
Return the list of all the delays (float values)
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Takes in 2 int arguments and
       spawn wait_random n times with the specified max_delay.
       Return:
       - list of all the delays (float values).
    """
    res = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(res)


if __name__ == "__main__":
    asyncio.run(wait_n(5, 5))
