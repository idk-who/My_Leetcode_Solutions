class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        
        temp, window = 0, 0
        for i in range(len(nums)*2):
            if nums[i%len(nums)]: temp += 1
            if i >= ones and nums[(i-ones)%len(nums)]: temp -= 1
            window = max(window, temp)
        
        return ones - window
