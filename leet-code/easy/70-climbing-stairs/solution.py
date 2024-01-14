class Solution:
    def climbStairs(self, n: int) -> int:
        pw = [0, 1]
        for i in range(2, n + 2):
            pw.append(pw[i - 2] + pw[i - 1])
        return pw[n + 1]
