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
        
        def rec(cuts, i, j, dp):
            if j - i == 1:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            mi = float('inf')
            for k in range(i+1, j):
                mi = min(
                    mi,
                    cuts[j] - cuts[i] + (
                        rec(cuts, i, k, dp) + 
                        rec(cuts, k, j, dp)
                    )
                )
            dp[(i, j)] = mi
            
            return mi
        
        return rec(cuts, 0, len(cuts)-1, dp)

