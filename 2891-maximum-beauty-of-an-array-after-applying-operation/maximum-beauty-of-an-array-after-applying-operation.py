class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        ans = 1
        for i in range(n):
            upper_bound = bisect.bisect(nums, nums[i]+2*k)
            ans = max(ans, upper_bound - i)
            
        return ans 

