import tests


# Time O(n^3)
# Space O(1)
def three_number_sum(array, target_sum):
    array.sort()
    results = []
    for i1 in range(len(array)):
        for i2 in range(i1 + 1, len(array)):
            for i3 in range(i2 + 1, len(array)):
                if array[i1] + array[i2] + array[i3] == target_sum:
                    results.append([array[i1], array[i2], array[i3]])
    return results


tests.test(three_number_sum)
