#!/usr/bin/python3
"""4-mru_cache
"""
from base_caching import BaseCaching
from collections import Counter


class MRUCache(BaseCaching):
    """MRUCache class
    """
    def __init__(self):
        """initialize
        """
        super().__init__()
        self._recent = []

    def put(self, key, item):
        """add new item
        """
        data = self.cache_data
        if key is not None and item is not None:
            data.update({key: item})
            if len(data.items()) > BaseCaching.MAX_ITEMS:
                old_key = self._recent[-1]
                print("DISCARD: {}".format(old_key))
                data.pop(old_key)
            self._recent.append(key)

    def get(self, key):
        """retrieve a new item
        """
        data = self.cache_data
        if key in data.keys():
            self._recent.append(key)
            val = data.get(key)
            return val
        return None
