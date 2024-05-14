class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.dp = [[True]*n for _ in range(m)]
        maxGold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxGold = max(maxGold, self.helper(grid, i, j, 0))
        return maxGold

    def helper(self, grid, i, j, gold):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and self.dp[i][j] and grid[i][j]):
            return gold
        self.dp[i][j] = False
        m = max(
            self.helper(grid, i+1, j, gold + grid[i][j]),
            self.helper(grid, i, j+1, gold + grid[i][j]),
            self.helper(grid, i-1, j, gold + grid[i][j]),
            self.helper(grid, i, j-1, gold + grid[i][j])
        )
        self.dp[i][j] = True

        return m