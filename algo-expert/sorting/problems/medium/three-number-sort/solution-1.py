import tests


# Time O(n)
# Space O(1)
def three_number_sort(array, order):
    left_not_sorted = 0
    for i in range(len(array)):
        if array[i] == order[0]:
            array[i], array[left_not_sorted] = array[left_not_sorted], array[i]
            left_not_sorted += 1
    right_not_sorted = len(array) - 1
    for i in reversed(range(left_not_sorted, len(array))):
        if array[i] == order[2]:
            array[i], array[right_not_sorted] = array[right_not_sorted], array[i]
            right_not_sorted -= 1
    return array


tests.test(three_number_sort)
