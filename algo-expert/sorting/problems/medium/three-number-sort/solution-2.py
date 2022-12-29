import tests


# Time O(n)
# Space O(1)
def three_number_sort(array, order):
    counts = {num: 0 for num in order}
    for num in array:
        counts[num] += 1

    i = 0
    for num, count in counts.items():
        for _ in range(count):
            array[i] = num
            i += 1
    return array


tests.test(three_number_sort)
