class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0

        for i in nums:
            if candidate == i:
                count += 1
            elif count <= 0:
                candidate = i
                count = 1
            else:
                count -= 1
        
        return candidate