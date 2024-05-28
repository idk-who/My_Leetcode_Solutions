class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        def calcCost(a, b):
            return abs(ord(a) - ord(b))
        
        p1 = 0
        p2 = 0

        cost = 0
        max_len = 0

        while p2 < len(s):
            cost += calcCost(s[p2], t[p2])
            while cost > maxCost:
                cost -= calcCost(s[p1], t[p1])
                p1 += 1
            max_len = max(max_len, p2-p1+1)

            p2 += 1
        
        return max_len
                
