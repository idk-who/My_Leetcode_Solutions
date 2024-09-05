class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_ind = [-1]*100

        ans = 0
        p1 = -1
        for p2, char in enumerate(s):
            if prev_ind[ord(char)-ord(' ')] > p1:
                p1 = prev_ind[ord(char)-ord(' ')]
            
            prev_ind[ord(char)-ord(' ')] = p2
            ans = max(ans, p2-p1)
        
        return ans
