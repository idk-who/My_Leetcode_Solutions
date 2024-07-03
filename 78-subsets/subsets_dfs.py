class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(nums, ptr, save):
            ans.append(save)
            for i in range(ptr, len(nums)):
                dfs(nums, i+1, save+[nums[i]])
        dfs(nums, 0, [])
        return ans
