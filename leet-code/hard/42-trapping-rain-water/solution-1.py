import tests


# Time O(n)
# Space O(1)
def trap(height):
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]
    rain = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            rain += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            rain += right_max - height[right]
    return rain


tests.test(trap)
