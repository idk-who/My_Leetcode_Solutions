class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ma = max(nums)

        ans = 1

        le = 1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i] == ma:
                le += 1
            else:
                le = 1
            ans = max(ans, le)
        
        return ans