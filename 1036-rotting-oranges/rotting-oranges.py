from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        n = len(grid)
        m = len(grid[0])
        ans = [[-1]*m for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2: q.append((i, j, 0))
        
        while q:
            i, j, t = q.popleft()
            if ans[i][j] != -1: 
                continue
            ans[i][j] = t
            
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if 0 <= i+di < n and 0 <= j+dj < m and grid[i+di][j+dj] == 1:
                    q.append((i+di, j+dj, t+1))

        ma = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if ans[i][j] == -1: return -1
                    ma = max(ma, ans[i][j])
            # print(ans[i])
        
        return ma
