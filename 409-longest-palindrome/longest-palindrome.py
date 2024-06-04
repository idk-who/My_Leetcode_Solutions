class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = [0]*58
        for i in s:
            freq[ord(i)-ord('a')] += 1
        
        ans = 0
        is_odd = 0
        for i in freq:
            if i & 1:
                is_odd = 1
            ans += (i>>1<<1)
        
        return ans + is_odd