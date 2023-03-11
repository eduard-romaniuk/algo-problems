from utils import testing
from binary_tree import BinaryTree


def test(func):
    n10 = BinaryTree(10)
    n9 = BinaryTree(9)
    n8 = BinaryTree(8)
    n7 = BinaryTree(7)
    n6 = BinaryTree(6)
    n5 = BinaryTree(5)
    n5.left = n10
    n4 = BinaryTree(4)
    n4.left = n8
    n4.right = n9
    n3 = BinaryTree(3)
    n3.left = n6
    n3.right = n7
    n2 = BinaryTree(2)
    n2.left = n4
    n2.right = n5
    n1 = BinaryTree(1)
    n1.left = n2
    n1.right = n3

    testing.test(name='#1', func=func, args=[n1], expected=[15, 16, 18, 10, 11])
