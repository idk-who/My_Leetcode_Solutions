class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0]*26

        for c in s:
            freq[ord(c)-ord('a')] += 1

        ans = 0

        for i in freq:
            if i&1:
                ans += 1
            elif i > 0:
                ans += 2
        
        return ans