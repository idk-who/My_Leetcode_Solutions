from collections import deque

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        
        flip = False 
        flip_ind = -1
        q = deque()
        for i in range(n-k+1):
            if len(q) > 0 and q[0] == i:
                flip = not flip
                q.popleft()
            real_bit = not nums[i] if flip else nums[i] 
            if real_bit == 0:
                ans += 1
                flip = not flip
                q.append(i + k)
        
        for i in range(n-k+1, n):
            if len(q) > 0 and q[0] == i:
                flip = not flip
                q.popleft()
            real_bit = not nums[i] if flip else nums[i] 
            if real_bit == 0:
                return -1
        return ans
