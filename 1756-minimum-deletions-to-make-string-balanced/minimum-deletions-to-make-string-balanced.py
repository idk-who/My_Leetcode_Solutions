class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = 0
        nb = 0
        for c in s:
            if c == 'a':
                dp = min(dp+1, nb)
            else:
                nb += 1
        
        return dp
