import tests


# Time O(2^n)
# Space O(n)
def nth_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return nth_fib(n - 1) + nth_fib(n - 2)


tests.test(nth_fib)
