import tests


# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selection_sort(array):
    for i in range(len(array)):
        i_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[i_min]:
                i_min = j
        array[i_min], array[i] = array[i], array[i_min]
    return array


tests.test(selection_sort)
