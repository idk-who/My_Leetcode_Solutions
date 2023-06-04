class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            t = target-numbers[i]
            left = i + 1
            right = len(numbers) - 1
            mid = (left + right) // 2

            while left <= right:
                if numbers[mid] == t:
                    return i+1, mid+1
                elif t > numbers[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left + right) // 2 

