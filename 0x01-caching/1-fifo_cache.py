#!/usr/bin/python3
"""1-fifo_cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class
    """
    def __init__(self):
        """initialize
        """
        super().__init__()

    def put(self, key, item):
        """add new item
        """
        data = self.cache_data
        if key is not None and item is not None:
            data.update({key: item})
            if len(data.items()) > BaseCaching.MAX_ITEMS:
                k = list(data)[0]
                print("DISCARD: {}".format(k))
                data.pop(k)

    def get(self, key):
        """retrieve a new item
        """
        data = self.cache_data
        if key in data.keys():
            return data.get(key)
        return None
