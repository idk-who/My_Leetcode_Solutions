class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s

        def pal(st, s, e):
            while s >= 0 and e < len(st) and st[s] == st[e]:
                s -= 1
                e += 1
            return st[s+1:e]
        
        ans = ""
        for i in range(len(s)-1):
            odd_pal = pal(s, i, i)
            even_pal = pal(s, i, i+1)
            
            if len(odd_pal) > len(ans):
                ans = odd_pal
            if len(even_pal) > len(ans):
                ans = even_pal
        
        return ans
