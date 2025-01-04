class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        suff = [0]*26

        for i in range(1, n):
            suff[ord(s[i])-ord('a')] += 1
    
        pref = [0]*26
        pref[ord(s[0])-ord('a')] += 1

        pals = set()
        for i in range(1, n-1):
            suff[ord(s[i])-ord('a')] -= 1

            cnt = 0
            for j in range(26):
                if min(pref[j], suff[j]) > 0:
                    pals.add(s[i]+chr(j+ord('a')))
                    
            print(i, cnt)

            pref[ord(s[i])-ord('a')] += 1
        
        return len(pals)