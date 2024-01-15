from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{"<-" if self.left else ""} {self.val} {"->" if self.right else ""}'


class Solution:
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        if not root.left or not root.right:
            return False
        left = [root.left]
        left_length = 1
        right = [root.right]
        right_length = 1
        while left_length == right_length != 0:
            for i in range(left_length):
                if (not left[i]) != (not right[i]):
                    return False
                if left[i] and right[i] and left[i].val != right[i].val:
                    return False
                if left[i]:
                    left.append(left[i].left)
                    left.append(left[i].right)
                if right[i]:
                    right.append(right[i].right)
                    right.append(right[i].left)
            left = left[left_length:]
            right = right[right_length:]
            left_length = len(left)
            right_length = len(right)
        return True

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
