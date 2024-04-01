#!/usr/bin/env python3
"""
Simple pagination helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function to create tuple pagination object

    args:
        page: page number
        page_size: size of elements

    return: tuple of page and page size
    """
    end_index: int = page * page_size
    start_index: int = end_index - page_size

    return tuple([start_index, end_index])
