class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            temp = Solution.bin_search(numbers, target-numbers[i])
            if temp != -1 and i != temp:
                return sorted([i+1, temp+1])

    
    def bin_search(nums, target):
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2 

        while left <= right:
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2 
        return -1

