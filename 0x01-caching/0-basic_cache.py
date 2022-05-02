#!/usr/bin/env python3

'''
Defines the caching module
'''

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Defines methods that add to and access from a dictinary.
    """

    def put(self, key, item):
        """Adds an item to the dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """accesses a dictionary item using a key and
           returns it if it exists
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)


if __name__ == '__main__':
    BasicCache = __import__('0-basic_cache').BasicCache

    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
