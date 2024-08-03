class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        def odd_pal(st, i):
            s = i-1
            e = i+1
            ans = 1
            while s >= 0 and e < len(st):
                if st[s] == st[e]:
                    ans += 2
                    s -= 1
                    e += 1
                else:
                    break
            return ans, s, e
        
        def even_pal(st, i):
            s = i
            e = i+1
            ans = 0
            while s >= 0 and e < len(st):
                if st[s] == st[e]:
                    ans += 2
                    s -= 1
                    e += 1
                else:
                    break
            return ans, s, e
        
        ans = 0
        ans_s = ""
        for i in range(len(s)-1):
            n1, s1, e1 = odd_pal(s, i)
            n2, s2, e2 = even_pal(s, i)
            if n1 > ans:
                ans = n1
                ans_s = s[s1+1:e1]
            if n2 > ans:
                ans = n2
                ans_s = s[s2+1:e2]
        
        return ans_s
