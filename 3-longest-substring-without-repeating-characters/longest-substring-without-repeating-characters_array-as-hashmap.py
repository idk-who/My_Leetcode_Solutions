class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = [-1]*95
        l = 0
        m = 0
        for ind, c in enumerate(s):
            if d[ord(c)-97]>=l:
                l = d[ord(c)-97] + 1
            m = max(m, ind - l + 1)
            d[ord(c)-97] = ind
        
        return m
