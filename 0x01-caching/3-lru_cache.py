#!/usr/bin/python3
"""3-lru_cache
"""
from base_caching import BaseCaching
from collections import Counter


class LRUCache(BaseCaching):
    """LRUCache class
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
                old_key = list(data.keys())[0]
                print("DISCARD: {}".format(old_key))
                data.pop(old_key)

    def get(self, key):
        """retrieve a new item
        """
        data = self.cache_data
        if key in data.keys():
            val = data.get(key)
            del data[key]
            data[key] = val
            return val
        return None
