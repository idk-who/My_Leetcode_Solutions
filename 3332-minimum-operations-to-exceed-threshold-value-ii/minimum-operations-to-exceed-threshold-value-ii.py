from heapq import heapify, heappop, heappush
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)

        ops = 0

        while nums[0] < k:
            ops += 1
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, min(x, y)*2+max(x, y))
        
        return ops