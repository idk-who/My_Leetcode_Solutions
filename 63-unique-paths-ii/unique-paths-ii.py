class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [0] * m
        for i in range(m):
            if obstacleGrid[0][i]:
                break
            dp[i] = 1

        for i in range(1, n):
            if obstacleGrid[i][0]:
                dp[0] = 0
            for j in range(1, m):
                if not obstacleGrid[i][j]:
                    dp[j] += dp[j-1]
                else:
                    dp[j] = 0
        
        return dp[-1]