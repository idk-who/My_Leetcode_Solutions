class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtracking(nums, 0)
        return self.ans
        
    def backtracking(self, nums, fi):
        if fi == len(nums)-1:
            self.ans.append(nums[:])
        
        for i in range(fi, len(nums)):
            nums[fi], nums[i] = nums[i], nums[fi]
            self.backtracking(nums, fi+1)
            nums[fi], nums[i] = nums[i], nums[fi]