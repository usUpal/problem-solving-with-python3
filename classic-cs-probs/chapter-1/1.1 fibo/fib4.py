# automatic memoizatin
'''
the decorator @functools.lru_cache() is used
with the same exact code as we used in fib2(). Each time fib4() is executed with a
novel argument, the decorator causes the return value to be cached. Upon future calls
of fib4() with the same argument, the previous return value of fib4() for that argument is retrieved from the cache and returned
'''
from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n) ->int:
    if n<2:
        return n
    return fib4(n-2) + fib4(n-1) # recursive case

if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))