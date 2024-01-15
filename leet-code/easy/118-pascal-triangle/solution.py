from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            res.append([1] * i)
            for j in range(len(res[-2]) // 2):
                res[-1][j + 1] = res[-1][len(res[-1]) - j - 2] = res[-2][j] + res[-2][j + 1]
        return res
