class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = []
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]: continue
            for j in range(i+1, n):
                if j > i+1 and nums[j-1] == nums[j]: continue
                p1 = j+1
                p2 = n-1

                tar = target - nums[i] - nums[j]

                while p1 < p2:
                    if nums[p1] + nums[p2] == tar:
                        ans.append(
                            [nums[i],nums[j], nums[p1], nums[p2]]
                        )
                        p1 += 1
                        while p1 < p2 and nums[p1-1] == nums[p1]:
                            p1 += 1 
                        p2 -= 1
                        while p1 < p2 and nums[p2+1] == nums[p2]:
                            p2 -= 1
                    elif nums[p1] + nums[p2] < tar:
                        p1 += 1
                    else:
                        p2 -= 1
            
        return ans
        