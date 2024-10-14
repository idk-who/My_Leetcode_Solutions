from heapq import heapify, heappush, heappop
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums[:] = [-i for i in nums]
        heapify(nums)

        score = 0

        while k:
            ele = - heappop(nums)
            score += ele

            ele = - (ele//3 + ((ele%3)>0))

            heappush(nums, ele) 
            k -= 1
        
        return score