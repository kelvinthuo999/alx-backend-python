#!/usr/bin/env python3
"""Function to return async function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> task:
    """Function to return async function"""
    task = create_task(wait_random(max_delay))
    return task
