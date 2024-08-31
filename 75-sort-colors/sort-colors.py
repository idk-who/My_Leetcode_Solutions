class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = two = 0

        for i in nums:
            if i == 0: zero += 1
            elif i == 1: one += 1
            else: two += 1

        for i in range(zero):
            nums[i] = 0
        
        for i in range(zero, zero+one):
            nums[i] = 1
        
        for i in range(zero+one, len(nums)):
            nums[i] = 2
        
        


        