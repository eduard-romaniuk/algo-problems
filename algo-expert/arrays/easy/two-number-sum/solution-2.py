import tests


# Time O(n)
# Space O(n)
def two_sum(array, target_sum):
    seen = set()
    for number in array:
        second_number = target_sum - number
        if second_number in seen:
            return [second_number, number]
        seen.add(number)
    return []


tests.test(two_sum)
