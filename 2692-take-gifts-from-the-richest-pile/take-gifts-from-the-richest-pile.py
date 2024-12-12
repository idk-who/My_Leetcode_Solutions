from heapq import heapify, heappop, heappush
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapify(gifts)
        
        for i in range(k):
            ele = -heappop(gifts)
            heappush(gifts, -int(ele**(1/2)))

        return -sum(gifts)