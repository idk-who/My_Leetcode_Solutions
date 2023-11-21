class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        n = len(nums)
        start = n - k

        for i in range(k):
            temp.append(nums[(i+start)%n])
        
        for i in range(n):
            temp.append(nums[i])
            nums[i] = temp.pop(0)
        
