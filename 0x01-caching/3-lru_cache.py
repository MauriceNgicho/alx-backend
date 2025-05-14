#!/usr/bin/env python3
"""LRU caching system"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A class that implements an LRU caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item to the cache using LRU replacement policy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove least recently used key
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Retrieve item by key and update its usage"""
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
