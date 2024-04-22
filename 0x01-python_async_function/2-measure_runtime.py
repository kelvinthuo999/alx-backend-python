#!/usr/bin/env python3
"""Function to measure elapsed time"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Func to measure elapsed time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    total_time = stop_time - start_time
    return total_time / n
