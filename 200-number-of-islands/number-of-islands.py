class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for i in range(n)]

        def DFS(grid, visited, i, j):
            visited[i][j] = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                    if grid[ni][nj] == '1' and not visited[ni][nj]:
                        DFS(grid, visited, ni, nj)
        
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    cnt += 1
                    DFS(grid, visited, i, j)
        
        return cnt