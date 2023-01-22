#!/usr/bin/env python3
"""
1-simple_pagination
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """find the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset
        """
        if isinstance(page, int) and isinstance(page_size, int):
            assert page > 0 and page_size > 0
            try:
                start = page_size * (page - 1)
                end = (page_size * page) + 1
                return self.__dataset[start:end]
            except(IndexError):
                return []
        else:
            raise(AssertionError)
