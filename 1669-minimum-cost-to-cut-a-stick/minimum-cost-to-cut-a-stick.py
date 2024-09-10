class Solution:
    def minCost(self, le: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [le]
        n = len(cuts)
        dp = [[float('inf')]*(n+1) for _ in range(n+1)]

        for i in range(n):
            dp[i][i+1] = 0

        for L in range(2, n):
            for i in range(1, n+1-L):
                j = i + L
                for k in range(i+1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        cuts[j-1] - cuts[i-1] + (
                            dp[i][k] + dp[k][j]
                        )
                    )
                    
        return dp[1][n]

