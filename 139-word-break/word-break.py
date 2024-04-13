class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.maxWL = max(map(len, wordDict))
        self.minWL = min(map(len, wordDict))
        self.words = set(wordDict)
        self.s = s
        self.dp = [None]*len(s)

        return self.helper(0)
    
    def helper(self, ptr = 0):
        if ptr == len(self.s): return True
        if ptr > len(self.s): return False
        if self.dp[ptr] is None:
            temp = []
            for i in range(ptr+self.minWL, ptr+self.maxWL+1):
                if self.s[ptr: i] in self.words:
                    temp.append(self.helper(i))
            print(temp)
            self.dp[ptr] = any(temp)
        return self.dp[ptr]                    