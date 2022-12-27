import tests


# Time O(n^2)
# Space O(1)
def subarray_sort(array):
    left = right = -1
    for i in range(1, len(array)):
        if array[i - 1] <= array[i]:
            continue
        right = i
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        if left == -1 or j < left:
            left = j
    return [left, right]


tests.test(subarray_sort)
