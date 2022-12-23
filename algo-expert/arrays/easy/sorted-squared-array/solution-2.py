import tests


# Space O(n)
# Time O(n)
def sorted_squared_array(array):
    result = []
    left = 0
    right = len(array) - 1
    while left <= right:
        if -array[left] > array[right]:
            result.append(array[left] ** 2)
            left += 1
        else:
            result.append(array[right] ** 2)
            right -= 1
    return result[::-1]


tests.test(sorted_squared_array)
