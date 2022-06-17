# Implement an LRU cache with the use of Redis

# Things to note:
# Python comes with the LRU cache decorator!
# @lru_cache(maxsize=None)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
# 
# >>> [fib(n) for n in range(16)]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
# 
# >>> fib.cache_info()
# CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)

# Note: setting the `maxsize` to None will allow the cache to grow indefinitely!

# AN LRU cache in Python is implemented using:
# - HashSeq, which is essentially a hash table that maps the function and its parameter to the return value
# - Doubly Linked list, which allows O(1) insertion and deletion from the front and back ends of the queue/list.

# Data types in Redis: https://redis.io/topics/data-types

# This file was copied from https://medium.com/@thebestchef/using-redis-in-python-lru-cache-56594df3582c

from collections import namedtuple
from functools import partial
import pickle
from my_redis import Client


WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')

WRAPPER_UPDATES = ('__dict__',)

def update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):
    """
    Update a wrapper function to look like the wrapped function.
    'wrapper' is the function to be updated.
    'wrapped' is the original function.
    'assigned' is a tuple naming the attributes assigned directly from the wrapped function to
    the wrapper function (defaults to functools.WRAPPER_ASSIGNMENTS).
    'updated' is a tuple naming the attributes of the wrapper that are updated with
    the corresponding attribute from the wrapped function (defaults to functools.WRAPPER_UPDATES).
    """
    
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)

    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    # Set __wrapped__ last so we don't inadvertently copy it from wrapped function when updating __dict__
    wrapper.__wrapped__ = wrapped
    # Return the wrapper so this can be used as a decorator via partial()
    return wrapper
    
def wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):
    """
    Decorator factory to apply update_wrapper() to a wrapper function.
    Returns a decorator that invokes update_wrapper() with the decorated function as
    the wrapper argument and the arguments to wraps() as the remaining arguments.
    Default arguments are as for update_wrapper(). This is a convenience function to
    simplify applying partial() to update_wrapper().
    """
    return partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)

_CacheInfo = namedtuple("CacheInfo", ["hits", "misses", "maxsize", "currsize"])

class _HashedSeq(list):
    """
    This class guarantees that hash() will be called no more than once per element.
    This is important because the lru_cache() will hash the key multiple times on a
    cache miss.
    """
    
    
    __slots__ = 'hashvalue'
    
    def __init__(self, tup, hash=hash):
        self[:] = tup
        self.hashvalue = hash(tup)
    
    def __hash__(self):
        return self.hashvalue


def _make_key(args, kwds, typed, kwd_mark = (object(),), fasttypes = {int, str}, tuple=tuple, type=type, len=len):
    """
    Make a cache key from optionally typed positional and keyword arguments. The key is
    constructed in a way that is as flat as possible rather than as a nested structure that would
    take more memory. If there is only a single argument and its data type is known to cache its hash
    value, then that argument is returned without a wrapper. This saves space and improves lookup speed.
    """
    # All of the code below relies on kwds preserving the order input by the user.
    # Formerly, we sorted() the kwds before looping. The new way is *much* faster; 
    # however, it means that f(x=1, y=2) will now be treated as a distinct call from 
    # f(y=2, x=1) which will be cached separately.
    key = args
    if kwds:
        key += kwd_mark
        for item in kwds.items():
            key += item
    if typed:
        key += tuple(type(v) for v in args)
        if kwds:
            key += tuple(type(v) for v in kwds.values())
    elif len(key) == 1 and type(key[0]) in fasttypes:
        return key[0]
    return _HashedSeq(key)
