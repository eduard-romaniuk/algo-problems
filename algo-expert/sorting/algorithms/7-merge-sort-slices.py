import tests


# Best: O(n*log(n)) time | O(n*log(n)) space
# Average: O(n*log(n)) time | O(n*log(n)) space
# Worst: O(n*log(n)) time | O(n*log(n)) space
def merge_sort(array):
    if len(array) == 1:
        return array

    center = len(array) // 2
    left_array = merge_sort(array[:center])
    right_array = merge_sort(array[center:])

    result = []
    right_index = left_index = 0
    while right_index < len(left_array) and left_index < len(right_array):
        if left_array[right_index] < right_array[left_index]:
            result.append(left_array[right_index])
            right_index += 1
        else:
            result.append(right_array[left_index])
            left_index += 1
    while right_index < len(left_array):
        result.append(left_array[right_index])
        right_index += 1
    while left_index < len(right_array):
        result.append(right_array[left_index])
        left_index += 1
    return result


tests.test(merge_sort)
