import tests


# Time O(n*log(n))
# Space O(1)
def two_sum(array, target_sum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == target_sum:
            return [array[left], array[right]]
        if current_sum > target_sum:
            right -= 1
        else:
            left += 1
    return []


tests.test(two_sum)
