import tests


def merge(array, result, start, center, end):
    ri = start
    i1 = start
    i2 = center + 1
    while i1 <= center and i2 <= end:
        if array[i1] <= array[i2]:
            result[ri] = array[i1]
            i1 += 1
        else:
            result[ri] = array[i2]
            i2 += 1
        ri += 1

    while i1 <= center:
        result[ri] = array[i1]
        ri += 1
        i1 += 1
    while i2 <= end:
        result[ri] = array[i2]
        ri += 1
        i2 += 1


def _merge_sort(array, result, start, end):
    if start == end:
        return
    center = (start + end) // 2
    _merge_sort(result, array, start, center)
    _merge_sort(result, array, center + 1, end)
    merge(array, result, start, center, end)


# Best: O(n*log(n)) time | O(n) space
# Average: O(n*log(n)) time | O(n) space
# Worst: O(n*log(n)) time | O(n) space
def merge_sort(array):
    if len(array) <= 1:
        return array
    _merge_sort(array[:], array, 0, len(array) - 1)
    return array


tests.test(merge_sort)
