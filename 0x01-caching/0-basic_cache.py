#!/usr/bin/python3
"""0-basic_cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache
    """
    def __init__(self):
        """initilaize
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """add to cache_data
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """retrieve item linked to key
        """
        data = self.cache_data
        if key in data.keys():
            return data.get(key)
        return None
