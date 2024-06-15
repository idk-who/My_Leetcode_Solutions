from heapq import heappop, heappush
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # cd = defaultdict(list)

        # for i in range(len(capital)):
        #     cd[capital[i]].append(profits[i])
        
        # for i in cd:
        #     cd[i].sort()

        cp = []
        for c, p in zip(capital, profits):
            heappush(cp, (c, p))

        ans = w
        h = []
        while k and w >= 0:
            while len(cp) > 0 and cp[0][0] <= w:
                c, p = heappop(cp)
                heappush(h, (-p, c))
            
            while len(h) > 0 and h[0][1] > w:
                p, c = heappop(h)
                heappush(cp, (c, -p))
            
            if len(h) == 0:
                break

            p, c = heappop(h)
            p = -p
            ans += p
            w = w + p

            k -= 1
        
        return ans