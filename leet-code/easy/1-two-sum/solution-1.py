import tests


# Time O(n^2)
# Space O(1)
def two_sum(array, target_sum):
    for i, number in enumerate(array):
        for j, second_number in enumerate(array[i + 1:], start=i + 1):
            if number + second_number == target_sum:
                return [i, j]
    return []


tests.test(two_sum)
