import tests


# Time O(n)
# Space O(n)
def zero_sum_subarray(nums):
    sums = set([0])
    sum = 0
    for num in nums:
        sum += num
        if sum in sums:
            return True
        sums.add(sum)
    return False


tests.test(zero_sum_subarray)
