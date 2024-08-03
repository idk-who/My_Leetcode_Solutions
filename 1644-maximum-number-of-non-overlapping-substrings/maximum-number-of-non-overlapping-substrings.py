class Solution:
    def maxNumOfSubstrings(self, string: str) -> List[str]:
        fst = { s:i for i, s in reversed(list(enumerate(string))) }
        lst = { s:i for i, s in enumerate(string) }

        intervals = []

        for c in set(string):
            b = fst[c]
            e = lst[c]
            ptr = b
            while ptr < e and b == fst[c]:
                b = min(b, fst[string[ptr]])
                e = max(e, lst[string[ptr]])
                ptr += 1
            if b == fst[c]:
                intervals.append([b, e])
        
        intervals.sort(key = lambda x: x[1])

        ans = []
        prev = -1
        for b, e in intervals:
            if b > prev:
                prev = e
                ans.append(string[b:e+1])
        
        return ans