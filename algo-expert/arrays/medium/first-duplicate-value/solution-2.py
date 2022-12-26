import tests


# Time O(n)
# Space O(1)
# Quite hacky solution that is possible due to constraint that all values in array in range from 1 to len(array),
# so we know that we wouldn't jump out of array when accessing n - 1 element
def first_duplicate_value(array):
    for n in array:
        n = abs(n)
        if array[n - 1] < 0:
            return n
        array[n - 1] *= -1
    return -1


tests.test(first_duplicate_value)
