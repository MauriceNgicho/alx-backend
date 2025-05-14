#!/usr/bin/env python3
""" FIFO Cache module """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()

    def put(self, key, item):
        """Add item to cache using FIFO"""
        if key is None or item is None:
            return

        #  Add/replace an item
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            #  Get the first key inserted
            first_key = next(iter(self.cache_data))
            #  Remove the first key
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Get item from cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
