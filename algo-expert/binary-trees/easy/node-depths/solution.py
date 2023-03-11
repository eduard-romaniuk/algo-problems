import tests
from binary_tree import BinaryTree


# Time O(n)
# Space O(h) - where h is the height of the Binary Tree. We are storing calls stack.
def node_depths(root: BinaryTree, depth=0):
    if root is None:
        return 0
    lb = node_depths(root.left, depth + 1)
    rb = node_depths(root.right, depth + 1)
    return depth + lb + rb


tests.test(node_depths)
