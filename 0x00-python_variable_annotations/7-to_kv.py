#!/usr/bin/env python3
"""Function to square the second item in a tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing k and the square of v."""
    return (k, v ** 2)
