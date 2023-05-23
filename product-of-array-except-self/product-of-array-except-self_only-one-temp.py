class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i-1]*nums[i-1]

        temp = 1
        for i in range(len(nums)-2, -1, -1):
            temp *= nums[i+1]
            answer[i] *= temp

        return answer
