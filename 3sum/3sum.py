class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []
        for i in range(len(nums)):
            target = -nums[i]
            l = i+1
            r = len(nums)-1
            while (l < r):
                temp = nums[l] + nums[r]
                if temp == target:
                    ans = [nums[i], nums[l], nums[r]]
                    if ans not in answers:
                        answers.append(ans)
                    l += 1
                elif temp < target:
                    l += 1
                else:
                    r -= 1

        return answers