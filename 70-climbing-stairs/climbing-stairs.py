class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = dict()
        return self.helper(n)
    def helper(self, n):
        if n == 0 or n == 1: return 1
        if (n, 1) not in self.dp:
            self.dp[(n, 1)] = self.helper(n-1)
        if (n, 2) not in self.dp:
            self.dp[(n, 2)] = self.helper(n-2)
        return self.dp[(n, 1)] + self.dp[(n, 2)] 
