class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1]*(len(text2)) for _ in range(len(text1))]
        # print(dp)
        def helper(t1, t2, p1, p2, dp):
            # print(p1, p2)
            if p1 == len(t1) or p2 == len(t2):
                return 0
            if dp[p1][p2] == -1:
                dp[p1][p2] = max(
                    (t1[p1] == t2[p2]) + helper(t1, t2, p1+1, p2+(t1[p1] == t2[p2]), dp),
                    (t1[p1] == t2[p2]) + helper(t1, t2, p1+(t1[p1] == t2[p2]), p2+1, dp)
                )
            return dp[p1][p2]
        
        return helper(text1, text2, 0, 0, dp)