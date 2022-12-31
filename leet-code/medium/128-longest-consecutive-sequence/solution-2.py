import tests


# Time O(n)
# Space O(n)
def longest_consecutive(nums):
    nums_set = set(nums)
    max_length = 0
    while nums_set:
        left = right = nums_set.pop()
        while left - 1 in nums_set:
            left -= 1
            nums_set.remove(left)
        while right + 1 in nums_set:
            right += 1
            nums_set.remove(right)
        max_length = max(max_length, right - left + 1)
    return max_length


tests.test(longest_consecutive)
