#!/usr/bin/env python3
"""Function to return a list of tuples"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples and its length."""
    return [(i, len(i)) for i in lst]
