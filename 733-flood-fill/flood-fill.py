class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        ptr = 0
        def dfs(image, i, j, c):
            org_c = image[i][j]
            image[i][j] = c

            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if 0 <= i+di < n and 0 <= j+dj < m and image[i+di][j+dj] == org_c:
                    dfs(image, i+di, j+dj, c)
        
        if image[sr][sc] != color:
            dfs(image, sr, sc, color)
        
        return image