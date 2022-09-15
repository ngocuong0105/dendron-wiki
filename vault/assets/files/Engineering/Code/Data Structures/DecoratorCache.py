#%%
from LRUCache import LRUCache

def cache(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

def lru_cache(func):
    cache = LRUCache(100)
    def wrapper(n):
        if n not in cache.cache:
            cache.put(n, func(n))
        return cache.get(n)
    return wrapper

def lru_cache_capacity(capacity):
    def lru_cache(func):
        if capacity == None: capacity
        cache = LRUCache(capacity)
        def wrapper(n):
            if n not in cache.cache:
                cache.put(n, func(n))
            return cache.get(n)
        return wrapper
    return lru_cache

@cache
def cached_fib(n):
    if n <= 2: return 1
    return cached_fib(n-1) + cached_fib(n-2)

@lru_cache
def lru_cached_fib(n):
    if n <= 2: return 1
    return lru_cached_fib(n-1) + lru_cached_fib(n-2)

@lru_cache_capacity(50)
def lru_cached_fib(n):
    if n <= 2: return 1
    return lru_cached_fib(n-1) + lru_cached_fib(n-2)


# %%
def memoize(fn):
    cache = {}
    def wrapper(*args):
        key = str(args)
        if key not in cache:
            cache[key] = fn(*args)
        return cache[key]
    return wrapper

@memoize
def cached_sum(nums):
    return sum(nums)

# %%