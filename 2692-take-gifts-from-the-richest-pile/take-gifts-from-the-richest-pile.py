from heapq import heapify, heappop, heappush
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        ans = 0
        h = []
        
        for g in gifts:
            if len(h) < k:
                heappush(h, g)
            else:
                if h[0] >= g:
                    ans += g
                else:
                    ans += heappop(h)
                    heappush(h, g)
        
        h = [-i for i in h]
        heapify(h)
        
        for i in range(k):
            heappush(h, -int((-heappop(h))**(1/2)))
        ans += -sum(h)

        return ans

