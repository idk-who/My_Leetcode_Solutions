from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        flip_cnt = 0

        for i in range(n):
            if i >= k and nums[i-k] >= 2:
                flip_cnt -= 1
                nums[i-k] -= 2  

            if flip_cnt & 1 == nums[i]:
                if i > n-k:
                    return -1
                
                ans += 1
                flip_cnt += 1
                nums[i] += 2
                
        return ans
