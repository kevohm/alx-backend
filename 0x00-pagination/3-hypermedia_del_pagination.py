#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        index: the current start index of the return page".
        next_index: the next index to query with.
        page_size: the current page size
        data: the actual page of the dataset
        """
        data = self.indexed_dataset()
        page = math.ceil(index / page_size)
        end = index + page_size
        assert index < 1000 and index > -1
        d = []
        i = index
        while i < end:
            try:
                d.append(data[i])
            except(KeyError):
                end += 1
            i += 1
        return {"index": index, "data": d,
                "page_size": len(d), "next_index": end}
