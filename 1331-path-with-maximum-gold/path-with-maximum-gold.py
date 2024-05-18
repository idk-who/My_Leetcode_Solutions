class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        maxGold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxGold = max(maxGold, self.helper(grid, i, j, 0))
        return maxGold

    def helper(self, grid, i, j, gold):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j]):
            return gold
        temp = grid[i][j]
        grid[i][j] = 0
        m = max(
            self.helper(grid, i+1, j, gold + temp),
            self.helper(grid, i, j+1, gold + temp),
            self.helper(grid, i-1, j, gold + temp),
            self.helper(grid, i, j-1, gold + temp)
        )
        grid[i][j] = temp

        return m