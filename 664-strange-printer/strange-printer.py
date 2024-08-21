class Solution:
    def strangePrinter(self, s: str) -> int:
        # String processing refer to lee215 - https://leetcode.com/problems/strange-printer/discuss/106794/One-suggestion-for-all-solutions
        S = ''.join(a for a, b in zip(s, '#' + s) if a != b)
        # S = re.sub(r'(.)\1*', r'\1', s)
        
        @lru_cache(None)
        # dp(i, j) is the number of turns needed to print S[i:j]
        def dp(i, j):
            if i == j: return 0
            ans = dp(i, j-1) + 1
            for k in range(i, j-1):
                if S[k] == S[j-1]:
                    ans = min(ans, dp(i, k+1) + dp(k+1, j-1))
            return ans
    
        return dp(0, len(S))   