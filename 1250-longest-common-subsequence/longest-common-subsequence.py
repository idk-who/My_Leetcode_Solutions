class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def rec(t1, t2, p1, p2, dp):
            if p1 == len(t1) or p2 == len(t2):
                return 0
            if (p1, p2) in dp:
                return dp[(p1, p2)]
            
            if t1[p1] == t2[p2]:
                ma = 1 + rec(t1, t2, p1+1, p2+1, dp)
            else:
                ma = max(
                    rec(t1, t2, p1+1, p2, dp),
                    rec(t1, t2, p1, p2+1, dp)
                )
            
            dp[(p1, p2)] = ma
            return ma
        
        return rec(text1, text2, 0, 0, dict())