#!/usr/bin/env python3
"""Function to return async function"""
from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Function to return async function"""
    task = create_task(wait_random(max_delay))
    return task
