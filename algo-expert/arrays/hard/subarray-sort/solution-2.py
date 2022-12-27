import tests


# Time O(n)
# Space O(1)
def subarray_sort(array):
    biggest = -float('inf')
    smallest = float('inf')
    for i in range(len(array)):
        if i == 0 and array[i] <= array[i + 1] or \
                i == len(array) - 1 and array[i - 1] <= array[i] or \
                array[i - 1] <= array[i] <= array[i + 1]:
            continue
        smallest = min(smallest, array[i])
        biggest = max(biggest, array[i])
    if smallest == float('inf'):
        return [-1, -1]
    left = 0
    while array[left] <= smallest:
        left += 1
    right = len(array) - 1
    while array[right] >= biggest:
        right -= 1
    return [left, right]


tests.test(subarray_sort)
