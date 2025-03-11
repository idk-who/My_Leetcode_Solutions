class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = [0]*3
        left = 0
        ans = 0
        for right in range(len(s)):
            freq[ord(s[right])-ord('a')] += 1

            while all(freq):
                ans += len(s) - right
                freq[ord(s[left])-ord('a')] -= 1
                left += 1
        
        return ans