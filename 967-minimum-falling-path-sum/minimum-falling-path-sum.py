class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]
        temp = [0]*n

        for i in range(1, n):
            for j in range(n):
                temp[j] = dp[j]
                if j > 0:
                    temp[j] = min(temp[j], dp[j-1])
                if j < n-1:
                    temp[j] = min(temp[j], dp[j+1])
                temp[j] += matrix[i][j]
            dp[:] = temp
        
        return min(dp)