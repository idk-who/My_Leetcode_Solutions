from heapq import heapify, heappop, heappush

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        h = []
        heapify(h)
        hand.sort()
        for i in hand:
            # print(i, h)
            if len(h) == 0:
                for s in range(1, groupSize):
                    heappush(h, i+s)
            else:
                ele = heappop(h)
                if ele < i:
                    return False
                elif ele > i:
                    heappush(h, ele)
                    for s in range(1, groupSize):
                        heappush(h, i+s)
        
        return len(h) == 0