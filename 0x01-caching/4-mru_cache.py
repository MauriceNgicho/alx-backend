#!/usr/bin/env python3
"""MRU caching system"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Most Recently Used caching system"""

    def __init__(self):
        """Initialize the cache and usage tracker"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item to cache using MRU policy"""
        if key is None or item is None:
            return

        # If key already in cache, remove it from usage tracking
        if key in self.cache_data:
            self.usage_order.remove(key)

        # If cache is full and key is new, discard MRU key (last used)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.usage_order.pop(-1)  # Remove last used key
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add/update the key in cache and usage tracker
        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """Retrieve item by key and update usage"""
        if key is None or key not in self.cache_data:
            return None

        # Since accessed, refresh usage: remove and add to end
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
