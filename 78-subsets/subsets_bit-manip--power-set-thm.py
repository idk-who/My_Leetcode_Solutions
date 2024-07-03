class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        set_size = 2**(len(nums))
        for i in range(set_size):
            temp = []
            for j in range(len(nums)):
                if i & (1 << j):
                    temp.append(nums[j])
            ans.append(temp)
        return ans

