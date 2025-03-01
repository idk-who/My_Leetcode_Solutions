class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        zeros = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == nums[i+1]:
                ans.append(2*nums[i])
                nums[i+1] = 0
            else:
                ans.append(nums[i])
        
        ans.append(nums[-1])
        ans += [0]*zeros

        return ans