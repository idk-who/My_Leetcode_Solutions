class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        ans = 1
        j = 0
        for i in range(1, n):
            if nums[i] - nums[j] <= 2*k:
                ans = max(ans, i-j+1)
            else:
                while nums[i] - nums[j] > 2*k:
                    j += 1

        return ans 

