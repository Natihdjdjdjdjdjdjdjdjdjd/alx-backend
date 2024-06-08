#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """that is a range from a given page and page size.
    """
    begin = (page - 1) * page_size
    end = begin + page_size
    return (begin, end)
