class Solution:
    def minOperations(self, nums: List[int]) -> int:
        _max = nums[0]+1
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] < _max:
                ans += _max - nums[i]
            _max = max(_max, nums[i]) + 1
        
        return ans