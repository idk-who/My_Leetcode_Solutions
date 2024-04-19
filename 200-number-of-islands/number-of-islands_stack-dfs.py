class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1
                    stack = [(i, j)]

                    while stack:
                        r, c = stack.pop()
                        grid[r][c] = '-1'
                        if r-1>=0 and grid[r-1][c] == '1':
                            stack.append((r-1, c))
                        if c-1>=0 and grid[r][c-1] == '1':
                            stack.append((r, c-1))
                        if r+1<n and grid[r+1][c] == '1':
                            stack.append((r+1, c))
                        if c+1<m and grid[r][c+1] == '1':
                            stack.append((r, c+1))
        
        return ans
