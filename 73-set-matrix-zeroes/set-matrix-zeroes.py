class Solution:
    def setZeroes(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(grid), len(grid[0])
        rows = [False]*n
        cols = [False]*m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        

        for i in range(n):
            for j in range(m):
                if rows[i] or cols[j]:
                    grid[i][j] = 0

        
