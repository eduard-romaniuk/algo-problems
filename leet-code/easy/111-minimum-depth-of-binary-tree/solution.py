from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        c = 1
        while q:
            l = len(q)
            for i in range(l):
                node = q.pop(0)
                if not node.left and not node.right:
                    return c
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            c += 1
        return c
