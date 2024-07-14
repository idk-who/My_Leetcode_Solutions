class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        ptr = 0
        visited = [[False]*m for _ in range(n)]
        def dfs(image, i, j, c):
            nonlocal visited
            if visited[i][j]:
                return
            org_c = image[i][j]
            image[i][j] = c
            visited[i][j] = True

            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if 0 <= i+di < n and 0 <= j+dj < m and image[i+di][j+dj] == org_c:
                    dfs(image, i+di, j+dj, c)
        
        dfs(image, sr, sc, color)
        
        return image