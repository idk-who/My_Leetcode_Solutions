class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        n, m = len(w1), len(w2)
        dp = [[float('inf')]*(m+1) for i in range(n+1)]

        def rec(w1, w2, p1, p2, dp):
            if p1 == len(w1):
                return m - p2
            if p2 == len(w2):
                return n - p1
            
            if dp[p1][p2] != float("inf"):
                return dp[p1][p2]
            
            if w1[p1] == w2[p2]:
                mi = rec(w1, w2, p1+1, p2+1, dp)
            else:
                mi = min(
                    1 + rec(w1, w2, p1+1, p2, dp),
                    1 + rec(w1, w2, p1, p2+1, dp),
                    1 + rec(w1, w2, p1+1, p2+1, dp)
                )
            
            dp[p1][p2] = mi

            return mi
        
        return rec(w1, w2, 0, 0, dp)
        
