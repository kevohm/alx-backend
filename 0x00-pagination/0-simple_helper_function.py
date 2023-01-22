#!/usr/bin/env python3
"""
0-simple_helper_function
"""


def index_range(page, page_size):
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start = page_size * (page - 1)
    end = page_size * page
    return (start, end)
