from heapq import heappush, heappop
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mi_h = []
        ma_h = []

        for ind, arr in enumerate(arrays):
            mi = arr[0]
            ma = arr[-1]

            heappush(mi_h, (mi, ind))
            heappush(ma_h, (-ma, ind))

        ma, ind1 = heappop(ma_h)
        mi, ind2 = heappop(mi_h)

        if ind1 != ind2:
            return -ma - mi
        
        ma2, ind1 = heappop(ma_h)
        mi2, ind2 = heappop(mi_h) 

        return max(
            -ma - mi2,
            -ma2 - mi
        )
            