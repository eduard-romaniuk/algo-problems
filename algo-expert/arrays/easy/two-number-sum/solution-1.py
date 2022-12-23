import tests


# Time O(n^2)
# Space O(1)
def two_sum(array, target_sum):
    for i, number in enumerate(array):
        for second_number in array[i + 1:]:
            if number + second_number == target_sum:
                return [number, second_number]
    return []


tests.test(two_sum)
