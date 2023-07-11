#!/usr/bin/env python3
"""
2-measure_runtime module
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    run_time = time.time()-start_time
    return run_time
