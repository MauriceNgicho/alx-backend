#!/usr/bin/env python3
"""LIFO caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A LIFO cache"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()

    def put(self, key, item):
        """Add an item using LIFO policy"""
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data):
            # Get the last inserted key
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve item by key"""
        return self.cache_data.get(key) if key is not None else None
