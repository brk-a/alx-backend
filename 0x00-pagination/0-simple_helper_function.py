#!/usr/bin/env python3

'''
return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.
'''

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing start index and end index
        corresponding to the range of indexes to ruturn in a list
    """
    return ((page - 1) * page_size, page * page_size)


if __name__ == '__main__':
    index_range = __import__('0-simple_helper_function').index_range

    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
