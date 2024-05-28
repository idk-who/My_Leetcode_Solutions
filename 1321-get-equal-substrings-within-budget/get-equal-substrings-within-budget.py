class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:   
        costs = []

        for i in range(len(s)):
            costs.append(abs(ord(s[i]) - ord(t[i])))
        
        p1 = 0
        p2 = 0

        cost = 0
        max_len = 0

        while p2 < len(s):
            cost += costs[p2]
            while cost > maxCost:
                cost -= costs[p1]
                p1 += 1
            max_len = max(max_len, p2-p1+1)

            p2 += 1
        
        return max_len
                
