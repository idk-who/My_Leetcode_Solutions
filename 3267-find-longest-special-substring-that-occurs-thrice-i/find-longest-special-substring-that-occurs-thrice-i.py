class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(int)

        d[(s[0], 1)] += 1
        le = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                le += 1
                d[(s[i], le)] += 1
                if le > 1:
                    d[(s[i], le-1)] += 1
                    if le > 2:
                        d[(s[i], le-2)] += 1
            else:
                le = 1
                d[(s[i], le)] += 1
            # print(d.items())
        ans = -1
        
        for (c, le), k in d.items():
            # print(c, le, k)
            if k >= 3:
                ans = max(ans, le)
        
        return ans





