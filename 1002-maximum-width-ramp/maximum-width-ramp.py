class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        temp = sorted([(nums[i], i) for i in range(len(nums))])
        ans = 0
        mi = float("inf")

        for ele, ind in temp:
            if ind < mi:
                mi = ind
            else:
                ans = max(ans, ind-mi)
        
        return ans
        

