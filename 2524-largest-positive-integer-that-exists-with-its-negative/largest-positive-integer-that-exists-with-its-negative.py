class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)

        ans = -1

        for i in nums:
            if i>0 and -i in nums and i>ans:
                ans = i
        
        return ans