from heapq import heappush, heappop, heapify
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [[-(((i+1)/(j+1))-i/j), i, j] for i, j in classes]
        heapify(heap)

        for _ in range(extraStudents):
            _, i, j = heappop(heap)
            i += 1
            j += 1
            heappush(heap, [-(((i+1)/(j+1))-i/j), i, j])

        su = sum([j/k for i, j, k in heap])
        return su/len(heap)

        
        

