class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0]*(len(text2)) for _ in range(len(text1))]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i][j] = (dp[i-1][j-1] + 1) if i > 0 and j > 0 else 1
                else:
                    dp[i][j] = max(
                        dp[i-1][j] if i > 0 else 0,
                        dp[i][j-1] if j > 0 else 0
                        )
        
        return dp[-1][-1]


