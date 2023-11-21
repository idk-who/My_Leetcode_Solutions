class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        queue = []
        n = len(nums)
        k = k % n
        
        for i in range(k):
            queue.append(nums[(i + n - k)])
        
        for i in range(n):
            queue.append(nums[i])
            nums[i] = queue.pop(0)
        
