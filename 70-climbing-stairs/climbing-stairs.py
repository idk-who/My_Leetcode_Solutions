class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = dict()
        return self.helper(n)
    def helper(self, n):
        if n == 0 or n == 1: return 1
        if n not in self.dp:
            self.dp[n] = self.helper(n-1) + self.helper(n-2)
        return self.dp[n]
