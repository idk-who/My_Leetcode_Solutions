from bisect import bisect
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n-1):
                if j != i+1 and nums[j-1] == nums[j]:
                    continue
                tar = - (nums[i]+nums[j])
                ind = bisect(nums, tar, lo=j+2) - 1
                if nums[ind] == tar:
                    ans.append([nums[i], nums[j], nums[ind]])
        return ans