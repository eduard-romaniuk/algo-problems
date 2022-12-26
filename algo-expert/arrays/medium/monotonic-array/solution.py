import tests


# Time O(n)
# Space O(1)
def is_monotonic(array):
    if len(array) < 3:
        return True
    last_diff = 0
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        if diff == 0:
            continue
        if diff > 0 > last_diff or diff < 0 < last_diff:
            return False
        last_diff = diff
    return True


tests.test(is_monotonic)
