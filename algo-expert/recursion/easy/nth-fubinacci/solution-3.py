import tests


# Time O(n)
# Space O(1)
def nth_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    previous = 0
    last = 1
    counter = 3
    while counter <= n:
        fib = previous + last
        previous = last
        last = fib
        counter += 1
    return last


tests.test(nth_fib)
