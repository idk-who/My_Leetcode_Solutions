class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            if not grid[row][0]:
                for j in range(len(grid[0])):
                    grid[row][j] = 0 if grid[row][j] else 1
        
        for col in range(len(grid[0])):
            if sum(row[col] for row in grid) < len(grid)/2:
                for i in range(len(grid)):
                    grid[i][col] = 0 if grid[i][col] else 1

        ans = 0
        for row in grid:
            temp = 0
            for col in row:
                temp <<= 1
                temp |= col
            ans += temp
        
        return ans
