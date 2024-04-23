#!/usr/bin/env python3
""" Function to run coroutine 10 times"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Function to generate random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
