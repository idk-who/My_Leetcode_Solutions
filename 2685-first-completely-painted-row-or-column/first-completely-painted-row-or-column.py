class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        indexes = dict()

        for i in range(m):
            for j in range(n):
                indexes[mat[i][j]] = (i, j)
        
        rows = [0]*m
        cols = [0]*n

        for i in range(len(arr)):
            ele = arr[i]

            r, c = indexes[ele]

            rows[r] += 1
            cols[c] += 1
            if rows[r] == n or cols[c] == m:
                return i
        
        return -1