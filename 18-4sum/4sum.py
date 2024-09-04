class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        d = {ele:ind for ind, ele in enumerate(nums)}
        ans = []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]: continue
            for j in range(i+1, n):
                if j > i+1 and nums[j-1] == nums[j]: continue
                for k in range(j+1, n):
                    if k > j+1 and nums[k-1] == nums[k]: continue
                    
                    tar = target - nums[i] - nums[j] - nums[k]
                    if tar in d and d[tar] > k:
                        ans.append(
                                [nums[i],nums[j], nums[k], tar]
                            )
            
        return ans
        
