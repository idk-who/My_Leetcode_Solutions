class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def max3x3(grid, i, j):
            m = grid[i][j]
            for i2 in range(i-1, i+2):
                for j2 in range(j-1, j+2):
                    m = max(m, grid[i2][j2])
            return m
        
        ans = []

        for i in range(1, len(grid)-1):
            temp = []
            for j in range(1, len(grid)-1):
                temp.append(max3x3(grid, i, j))
            ans.append(temp)

        return ans