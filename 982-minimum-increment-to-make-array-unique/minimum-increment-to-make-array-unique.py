class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[0]
        ans = 0
        # print(nums)
        for i in range(1, len(nums)):
            if nums[i] <= n:
                ans += n - nums[i] + 1
                n += 1
            else:
                n = nums[i]
            # print(n, ans)
        
        return ans