#!/usr/bin/python3
"""LET baash that inhert  che implementation Class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache implementaion class
    """
    def put(self, key, item):
        """ Add an item
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ get an item
        """
        return self.cache_data.get(key, None)
