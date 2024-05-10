import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = [(1/arr[i], 0, i) for i in range(len(arr))]

        heapq.heapify(heap)
        num, den = None, None
        while k:
            ans, num, den = heapq.heappop(heap)
            heapq.heappush(heap, (arr[num+1]/arr[den], num+1, den))
            k -= 1
        
        return [arr[num], arr[den]]
