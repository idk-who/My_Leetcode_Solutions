class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c = 0, 0, 0
        da = {0:-1}
        db = {0:-1}
        dc = {0:-1}
        ans = 0
        for i in range(len(s)):
            if s[i] == 'a':
                a += 1
                da[a] = i
            elif s[i] == 'b':
                b += 1
                db[b] = i
            else:
                c += 1
                dc[c] = i
            
            if a > 0 and b > 0 and c > 0:
                poss = min(
                    da[a],
                    db[b],
                    dc[c]
                ) + 1
                ans += poss
                # print(poss, da[a-1], db[b-1], dc[c-1])
        
        return ans