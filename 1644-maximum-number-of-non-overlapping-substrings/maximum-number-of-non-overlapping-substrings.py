class Solution:
    def maxNumOfSubstrings(self, s):
        fst = { c : i for i, c in reversed(list(enumerate(s))) }
        lst = { c : i for i, c in enumerate(s) }
        
        ans, prev = [], -1
        for i in sorted(lst.values()):
            b, e = fst[s[i]], lst[s[i]]
            j = e
            while j >= b and b > prev and e == i:
                b = min(b, fst[s[j]])
                e = max(e, lst[s[j]])
                j -= 1
            if b > prev and e == i:
                ans.append(s[b:e + 1])
                prev = e
        
        return ans