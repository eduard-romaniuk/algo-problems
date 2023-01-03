def search(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        center = (start + end) // 2
        if nums[center] == target:
            return center
        if nums[center] > target:
            end = center - 1
        else:
            start = center + 1
    return -1
