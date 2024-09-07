class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [0]*(len(text2))
        dp2 = [0]*(len(text2))
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp2[j] = (dp[j-1] + 1) if j > 0 else 1
                else:
                    dp2[j] = max(
                        dp2[j],
                        dp2[j-1] if j > 0 else 0
                        )
            dp[:] = dp2

        return dp[-1]




