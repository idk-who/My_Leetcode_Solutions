class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i-1 <0            or grid[i-1][j] == 0:
                        ans += 1
                    if j-1 <0            or grid[i][j-1] == 0:
                        ans += 1
                    if i+1>=len(grid)    or grid[i+1][j] == 0:
                        ans += 1
                    if j+1>=len(grid[0]) or grid[i][j+1] == 0:
                        ans += 1
        
        return ans
