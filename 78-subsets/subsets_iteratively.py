class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(len(nums)):
            ans += [ele+[nums[i]] for ele in ans]

        return ans

    
