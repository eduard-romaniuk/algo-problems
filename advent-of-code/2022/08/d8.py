from functools import reduce
from operator import mul as multiply

# Common
trees = [[int(tree) for tree in line] for line in open('input.txt', 'r').read().split('\n')]
zip_trees = [list(i) for i in zip(*trees)]


def iterate(func):
    res = []
    for c in range(1, len(trees) - 1):
        for r in range(1, len(zip_trees) - 1):
            res.append(func(c, r))
    return res


# Task 1
def solution1(col, row):
    curr_tree_height = trees[col][row]
    views = [
        trees[col][:row],
        trees[col][:row:-1],
        zip_trees[row][:col],
        zip_trees[row][:col:-1]
    ]
    return 1 if any(map(lambda view: all(map(lambda tree_height: curr_tree_height > tree_height, view)), views)) else 0


print(f"Task 1: {(len(trees) * 4 - 4) + sum(iterate(solution1))}")


def scenic_score(examine_tree):
    def _scenic_score(tree_view):
        res = 0
        for tree in tree_view:
            res += 1
            if examine_tree <= tree:
                break
        return res

    return _scenic_score


def solution2(col, row):
    views = [
        trees[col][row - 1::-1],
        trees[col][row + 1:],
        zip_trees[row][col - 1::-1],
        zip_trees[row][col + 1:]
    ]
    return reduce(multiply, map(scenic_score(trees[col][row]), views))


print(f"Task 2: {max(iterate(solution2))}")
