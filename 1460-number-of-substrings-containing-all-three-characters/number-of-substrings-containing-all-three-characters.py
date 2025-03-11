class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_pos = [-1]*3
        ans = 0
        for i in range(len(s)):
            last_pos[ord(s[i])-ord('a')] = i
            
            ans += 1 + min(last_pos)
        
        return ans