from heapq import heappush, heappop

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mi_heap = []
        ma_heap = []

        start = 0
        max_len = 0

        for i in range(len(nums)):
            print()
            heappush(mi_heap, (nums[i], i))
            heappush(ma_heap, (-nums[i], i))

            if - ma_heap[0][0] - mi_heap[0][0] > limit:
                start = min(ma_heap[0][1], mi_heap[0][1]) + 1
                while ma_heap[0][1] < start: heappop(ma_heap)
                while mi_heap[0][1] < start: heappop(mi_heap)

            max_len = max(max_len, i-start+1)
        
        return max_len
            