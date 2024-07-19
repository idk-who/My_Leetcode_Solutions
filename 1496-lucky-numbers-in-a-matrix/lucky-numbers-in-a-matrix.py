class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_rows = list(map(lambda x: min(x), matrix))
        n, m = len(matrix), len(matrix[0])
        ans = []
        for j in range(m):
            ma = -1
            ma_i = -1
            for i in range(n):
                if matrix[i][j] > ma:
                    ma = matrix[i][j]
                    ma_i = i
            if ma == min_rows[ma_i]:
                ans.append(ma)
        
        return ans
