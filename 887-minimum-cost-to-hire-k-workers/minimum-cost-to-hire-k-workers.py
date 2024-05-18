from heapq import heapify, heappush, heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(wage)
        
        ratio = []
        for i in range(n):
            ratio.append((quality[i]/wage[i], quality[i]))
        ratio.sort(reverse=True)

        h = []
        heapify(h)
        total_quality = 0
        max_ratio = 0 
        min_cost = float("inf")

        for i in range(n):
            max_ratio = ratio[i][0]
            total_quality += ratio[i][1]
            heappush(h, -ratio[i][1])

            if len(h) == k:
                min_cost = min(min_cost, total_quality/max_ratio)
                total_quality += heappop(h)
        
        return min_cost