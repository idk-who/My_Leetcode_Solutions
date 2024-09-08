class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[-1]*m for _ in range(n)]
        def rec(grid, i, j):
            if i == n - 1 and j == m - 1:
                return grid[i][j]
            if i == n or j == m:
                return float('inf')
            if dp[i][j] != -1:
                return dp[i][j]
            
            mi = grid[i][j] + min(
                rec(grid, i+1, j),
                rec(grid, i, j+1)
            )

            dp[i][j] = mi
            return mi
        
        return rec(grid, 0, 0)