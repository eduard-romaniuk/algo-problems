import tests


# Time O(n)
# Space O(n)
def nth_fib(n, cache={1: 0, 2: 1}):
    if n in cache:
        return cache[n]
    cache[n] = nth_fib(n - 1, cache) + nth_fib(n - 2, cache)
    return cache[n]


tests.test(nth_fib)
