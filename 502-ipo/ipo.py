from heapq import heappop, heappush
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # cd = defaultdict(list)

        # for i in range(len(capital)):
        #     cd[capital[i]].append(profits[i])
        
        # for i in cd:
        #     cd[i].sort()

        cp = []
        h = []
        for c, p in zip(capital, profits):
            if c > w:
                heappush(cp, (c, p))
            else:
                heappush(h, (-p, c)) 

        while k and h:
            p, c = heappop(h)
            w -= p
            
            while len(cp) > 0 and cp[0][0] <= w:
                c, p = heappop(cp)
                heappush(h, (-p, c))

            k -= 1
        
        return w