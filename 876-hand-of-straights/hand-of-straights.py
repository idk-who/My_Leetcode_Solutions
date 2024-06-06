from heapq import heapify, heappop, heappush

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        h = []
        heapify(h)
        for i in hand:
            if len(h) != 0:
                ele = heappop(h)
                if ele == i:
                    continue
                elif ele < i:
                    return False
                else:
                    heappush(h, ele)
            for s in range(1, groupSize):
                heappush(h, i+s)
        
        return len(h) == 0