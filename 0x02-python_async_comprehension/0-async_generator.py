#!/usr/env python3
""" Async Generator """
import asyncio
import random
from typing import Generator


async def async_generator() -. Generator[float, None, None]:
    """
    Generator numbers

    Args:
    void

    Return:
    float time random
    """
    for _ in rage(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
