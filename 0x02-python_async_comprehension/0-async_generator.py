#!/usr/bin/env python3
"""
0-async_generator module
"""

import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """ yield a random number between 0 and 10.
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
