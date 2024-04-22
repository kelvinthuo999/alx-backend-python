#!/usr/bin/env python3
"""Function to return async function"""
import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """Function to return async function"""
    return asyncio.create_task(wait_random(max_delay))
