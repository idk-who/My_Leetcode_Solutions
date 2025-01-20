class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        indexes = dict()

        for i in range(len(arr)):
            indexes[arr[i]] = i
        
        ans = float('inf')
        
        for i in range(m):
            ma = float('-inf')
            for j in range(n):
                ma = max(
                    ma,
                    indexes[mat[i][j]]
                )
            ans = min(ans, ma)

        for j in range(n):
            ma = float('-inf')
            for i in range(m):
                ma = max(
                    ma,
                    indexes[mat[i][j]]
                )
            ans = min(ans, ma)

        return ans