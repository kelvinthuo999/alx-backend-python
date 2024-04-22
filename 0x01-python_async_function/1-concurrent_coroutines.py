#!/usr/bin/env python3
"""Function to return a list of delays"""
from typing import List
import random
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function to return a list of delays"""
    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(delays)]
