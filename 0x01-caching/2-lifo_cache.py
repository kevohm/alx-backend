#!/usr/bin/python3
"""2-lifo_cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class
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
            if len(data.items()) >= BaseCaching.MAX_ITEMS:
                k = list(data)[-1]
                print("DISCARD: {}".format(k))
                data.pop(k)
            data.update({key: item})

    def get(self, key):
        """retrieve a new item
        """
        data = self.cache_data
        if key in data.keys():
            return data.get(key)
        return None
