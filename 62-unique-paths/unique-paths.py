class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def rec(i, j, dp):
            if i == m-1 and j == n-1:
                return 1
            if i == m or j == n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            ma = rec(i+1, j, dp) + rec(i, j+1, dp)
            dp[(i, j)] = ma
            return ma
        
        return rec(0, 0, dict())