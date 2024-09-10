class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wd = set(wordDict)
        mi = len(min(wordDict, key = len))
        ma = len(max(wordDict, key = len))
        dp = dict()

        def rec(ptr, dp):
            if ptr == len(s):
                return True
            if ptr in dp:
                return dp[ptr]
            
            po = False
            for i in range(mi, ma+1):
                if s[ptr:ptr+i] in wd:
                    if rec(ptr+i, dp):
                        po = True
                        break
            dp[ptr] = po
            
            return po

        return rec(0, dp)
