class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            t = target-numbers[i]
            left = i + 1
            right = len(numbers) - 1
            mid = (left + right) // 2 
            temp = -1
            while left <= right:
                if numbers[mid] == t:
                    temp = mid
                    break
                elif t > numbers[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                mid = (left + right) // 2 

            if temp != -1:
                return i+1, temp+1
        return [-1, -1]

