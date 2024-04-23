#!/usr/bin/env python3
""" Function to run coroutine 10 times"""
import random
import asyncio


async def async_generator():
    """Function to generate random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
