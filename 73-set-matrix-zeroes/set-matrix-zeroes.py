class Solution:
    def setZeroes(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(grid), len(grid[0])
        col_zero = 1

        for i in range(n):
            if grid[i][0] == 0: col_zero = 0
            for j in range(1, m):
                if grid[i][j] == 0:
                    grid[i][0] = 0
                    grid[0][j] = 0

        for i in range(n-1, -1, -1):
            for j in range(m-1, 0, -1):
                if grid[i][0] == 0 or grid[0][j] == 0:
                    grid[i][j] = 0
            if col_zero == 0: grid[i][0] = 0
        
        

        
