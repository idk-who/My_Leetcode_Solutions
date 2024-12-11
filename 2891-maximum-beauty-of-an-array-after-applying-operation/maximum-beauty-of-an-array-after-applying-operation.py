class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        ma = 1
        for i in range(min(nums), max(nums)+1):
            l = bisect.bisect(nums, i-k)
            while 0 <= l < len(nums) and nums[l] >= i-k:
                l -= 1

            r = bisect.bisect(nums, i+k) - 1

            ma = max(ma, r-l)
        
        return ma

