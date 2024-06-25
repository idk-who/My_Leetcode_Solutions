class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = grid[0][:]

        for i in range(1, m):
            dp[i] += dp[i-1]

        for i in range(1, n):
            dp[0] += grid[i][0]
            for j in range(1, m):
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        
        return dp[-1]

                
