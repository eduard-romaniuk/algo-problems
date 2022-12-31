import tests


# Time O(n*log(n))
# Space O(1)
def longest_consecutive(nums):
    if len(nums) == 0:
        return 0
    nums.sort()
    max_length = 0
    current_length = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        if nums[i] - nums[i - 1] == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    return max(max_length, current_length)


tests.test(longest_consecutive)
