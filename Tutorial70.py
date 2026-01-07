# fucntion cashing
from functools import lru_cache
import time
  
@lru_cache(maxsize=None)
def fx(n):
    time.sleep(1)
    return n*5


for i in range(5):
    print(fx(i+1))
    print(f"Done for {i+1}")
    print("\n")

print("\n")

for i in range(7):
    print(fx(i))
    print(f"Done for {i}")
    print("\n")

fx.cache_clear() #If you want to clear the cache for a function-



for i in range(7):
    print(fx(i))
    print(f"Done for {i}")
    print("\n")

#NOTE
'''
Python provides a built-in way to achieve function caching using the functools.lru_cache decorator. The LRU (Least Recently Used) cache keeps track of the most recent function calls and caches the results up to a specified limit.

How to use lru_cache:
Import the decorator from functools.
Apply the decorator to the function you want to cache.

maxsize: Defines the maximum number of cached function calls. Once this limit is reached, the least recently used cache entries are discarded. If set to None, the cache will have unlimited size.
Advantages of Function Caching:
Improves performance for expensive or frequently called functions.
Reduces redundant calculations when the function is called multiple times with the same arguments
'''