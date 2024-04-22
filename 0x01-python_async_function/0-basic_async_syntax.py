#!/usr/bin/env python3
"""Function to run asynchronous routine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function to run concurrent routines"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
