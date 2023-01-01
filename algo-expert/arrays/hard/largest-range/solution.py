import tests


# Time O(n)
# Space O(n)
def largest_range(array):
    def range_size(left, right):
        return right - left + 1

    nums = set(array)
    max_range = [0, 0]
    while nums:
        num = nums.pop()
        left = right = num
        while left - 1 in nums:
            left -= 1
            nums.remove(left)
        while right + 1 in nums:
            right += 1
            nums.remove(right)
        current_range = [left, right]
        if range_size(*current_range) >= range_size(*max_range):
            max_range = current_range
    return max_range


tests.test(largest_range)
