import tests


# Time O(n)
# Space O(1)
def move_element_to_end(array, to_move):
    last = 0
    for i in range(len(array)):
        if array[i] != to_move:
            array[i], array[last] = array[last], array[i]
            last += 1
    return array


tests.test(move_element_to_end)
