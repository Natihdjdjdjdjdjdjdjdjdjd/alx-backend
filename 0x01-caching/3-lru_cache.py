#!/usr/bin/python3
"""Create LRUCache class that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ let summrize  LRUCache """

    def __init__(self):
        """ strat  LRUCache """
        self.mykey = []
        super().__init__()

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key and item:
            if self.cache_data.get(key):
                self.mykey.remove(key)
            self.mykey.append(key)
            self.cache_data[key] = item
            if len(self.mykey) > self.MAX_ITEMS:
                dele = self.mykey.pop(0)
                self.cache_data.pop(dele)
                print('DISCARD: {}'.format(dele))

    def get(self, key):
        """ retern valeue that associated with the given key """
        if self.cache_data.get(key):
            self.mykey.remove(key)
            self.mykey.append(key)
        return self.cache_data.get(key)
