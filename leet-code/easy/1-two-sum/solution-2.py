import tests


# Time O(n)
# Space O(n)
def two_sum(array, target_sum):
    seen = {}
    for i, number in enumerate(array):
        second_number = target_sum - number
        if second_number in seen:
            return [seen[second_number], i]
        seen[array[i]] = i
    return []


tests.test(two_sum)
