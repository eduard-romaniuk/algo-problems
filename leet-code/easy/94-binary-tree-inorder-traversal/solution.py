from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{"<-" if self.left else ""} {self.val} {"->" if self.right else ""}'


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
                pre.right = root
                tmp = root
                root = root.left
                tmp.left = None
            else:
                res.append(root.val)
                root = root.right
        return res

    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l = self.inorderTraversal(root.left)
        r = self.inorderTraversal(root.right)
        return l + [root.val] + r
