class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1]
        temp = 1

        for i in range(1, len(nums)):
            temp *= nums[i-1]
            answers.append(temp)
        
        temp = 1
        for i in range(len(nums)-2, -1, -1):
            temp *= nums[i+1]
            answers[i] *= temp
        
        return answers

