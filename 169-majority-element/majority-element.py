class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = -1
        count = 0

        for i in nums:
            if i == candidate:
                count += 1
            else:
                if count:
                    count -=1
                else:
                    candidate = i
                    count = 1
        
        return candidate