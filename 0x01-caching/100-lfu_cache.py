#!/usr/bin/python3
""" leety Create LFUCache class that inherits from BaseCaching """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Define LFUCache """

    def __init__(self):
        """ Initialize LFUCache """
        self.myqu = []
        self.lfu = {}
        super().__init__()

    def put(self, key, item):
        """ Assign the dictionary """
        if key and item:
            if (len(self.myqu) >= self.MAX_ITEMS and
                    not self.cache_data.get(key)):
                delete = self.myqu.pop(0)
                self.lfu.pop(delete)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

            if self.cache_data.get(key):
                self.myqu.remove(key)
                self.lfu[key] += 1
            else:
                self.lfu[key] = 0

            insert_index = 0
            while (insert_index < len(self.myqu) and
                   not self.lfu[self.myqu[insert_index]]):
                insert_index += 1
            self.myqu.insert(insert_index, key)
            self.cache_data[key] = item

    def get(self, key):
        """ The given key """
        if self.cache_data.get(key):
            self.lfu[key] += 1
            if self.myqu.index(key) + 1 != len(self.myqu):
                while (self.myqu.index(key) + 1 < len(self.myqu) and
                       self.lfu[key] >=
                       self.lfu[self.myqu[self.myqu.index(key) + 1]]):
                    self.myqu.insert(self.myqu.index(key) + 1,
                                      self.myqu.pop(self.myqu.index(key)))
        return self.cache_data.get(key)
