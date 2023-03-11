import tests
from binary_tree import BinaryTree

# Time O(n)
# Space O(n)
def branch_sums(root: BinaryTree):
    left_result = []
    right_result = []
    if root.left is not None:
        left_result = [root.value + v for v in branch_sums(root.left)]

    if root.right is not None:
        right_result = [root.value + v for v in branch_sums(root.right)]

    if left_result == right_result == []:
        return [root.value]

    return left_result + right_result


tests.test(branch_sums)
