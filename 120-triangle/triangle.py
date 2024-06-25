class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0]*n
        dp[0] = triangle[0][0]

        for i in range(1, n):
            temp = [0]*n
            temp[0] += triangle[i][0] + dp[0]
            temp[i] =  triangle[i][i] + dp[i-1]
            for j in range(1, i):
                temp[j] = triangle[i][j] + min(dp[j-1], dp[j])
            dp = temp
        
        return min(dp)