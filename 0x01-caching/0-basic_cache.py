#!/usr/bin/env python3
"""
caching module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A simple caching method with no limits"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None:
            return self.cache_data.get(key)
        return None
