from heapq import heappush, heappop
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) <= 2 or k <= 1:
            return 0
        n = len(weights)
        
        def helper(mul = 1, k = k):
            h = []
            for i in range(1, n):
                heappush(h, mul*(weights[i-1]+weights[i]))
            score = weights[0]+weights[-1]
            while k > 1:
                score += mul*(heappop(h))
                k -= 1
            return score
        
        return helper(-1) - helper(1)
