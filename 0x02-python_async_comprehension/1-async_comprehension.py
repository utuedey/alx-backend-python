#!/usr/bin/env python3
"""
1-async_comprehension module
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    random_number = [i async for i in async_generator()]
    return random_number
