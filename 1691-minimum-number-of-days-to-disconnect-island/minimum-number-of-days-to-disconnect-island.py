class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(vis, i, j):
            vis[i][j] = True

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i+di, j+dj
                
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] == 1 and not vis[ni][nj]:
                        dfs(vis, ni, nj)


        def is_disconnected():
            vis = [[False]*m for _ in range(n)]

            cnt = 0

            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1 and not vis[i][j]:
                        cnt += 1
                        dfs(vis, i, j)
            
            return cnt != 1
        

        if is_disconnected():
            return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if is_disconnected():
                        return 1
                    grid[i][j] = 1


        return 2

