class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = [None]*(n+1)
        return self.helper(n)
    def helper(self, n):
        if n < 2: return 1
        if self.dp[n] is None:
            self.dp[n] = self.helper(n-1) + self.helper(n-2)
        return self.dp[n]
