#!/usr/bin/python3
"""Create MRUCache class that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ let tell define MRUCache """

    def __init__(self):
        """ Initialize MRUCache """
        self.mystack = []
        super().__init__()

    def put(self, key, item):
        """ Assign the item to the dictionary """
        if key and item:
            if self.cache_data.get(key):
                self.mystack.remove(key)
            while len(self.mystack) >= self.MAX_ITEMS:
                dele = self.mystack.pop()
                self.cache_data.pop(dele)
                print('DISCARD: {}'.format(dele))
            self.mystack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value associated with the given key """
        if self.cache_data.get(key):
            self.mystack.remove(key)
            self.mystack.append(key)
        return self.cache_data.get(key)
