import tests


# Time O(n^2)
# Space O(1)
def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            triplet = [nums[i], nums[j], nums[k]]
            triplet_sum = sum(triplet)
            if triplet_sum == 0:
                result.append(triplet)
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            elif triplet_sum < 0:
                j += 1
            else:
                k -= 1
    return result


tests.test(three_sum)
