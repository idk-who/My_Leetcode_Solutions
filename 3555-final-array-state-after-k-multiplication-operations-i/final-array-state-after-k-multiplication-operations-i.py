from heapq import heapify, heappush, heappop
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = [(nums[i], i) for i in range(len(nums))] 
        heapify(h)
        for _ in range(k):
            n, i = heappop(h)
            nums[i] = n*multiplier
            heappush(h, (n*multiplier, i))

        return nums
