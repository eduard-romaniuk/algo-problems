from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int], start: int = 0, end: int = None) -> Optional[TreeNode]:
        if end is None:
            end = len(nums) - 1
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        center = (start + end) // 2
        return TreeNode(
            nums[center],
            self.sortedArrayToBST(nums, start, center - 1),
            self.sortedArrayToBST(nums, center + 1, end)
        )
