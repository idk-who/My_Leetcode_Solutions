class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        freq = [0]*26

        for c in s:
            freq[ord(c)-ord('a')] += 1
        
        odds = 0
        for i in range(26):
            if freq[i]&1:
                odds += 1
        
        if odds > k:
            return False
        
        return True