#!/usr/bin/env python3
"""Function to measure time"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def async_comprehension() -> float:
    start_time = time.time()
    job = [async_comprehension for item in range(4)]
    await gather(*job)
    end_time = time.time()
    return (end_time - start_time)
