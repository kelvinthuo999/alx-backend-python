#!/usr/bin/env python3
"""Function to return 10 random numbers"""
import asyncio
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Function to return 10 random numbers"""
    new_list = [item async for item in async_generator()]
    return new_list
