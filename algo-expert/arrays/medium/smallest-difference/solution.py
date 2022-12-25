import sys

import tests


# Time O(a1*log(a1) + a2*log(a2))
# Space O(1)
def smallest_difference(array_one, array_two):
    smallest = []
    smallest_diff = sys.maxsize
    array_one.sort()
    array_two.sort()
    i1 = 0
    i2 = 0

    while i1 < len(array_one) and i2 < len(array_two):
        abs_diff = abs(array_one[i1] - array_two[i2])
        if abs_diff < smallest_diff:
            smallest = [array_one[i1], array_two[i2]]
            smallest_diff = abs_diff
        if array_one[i1] > array_two[i2]:
            i2 += 1
        else:
            i1 += 1
    return smallest


tests.test(smallest_difference)
