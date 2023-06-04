class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        length = len(nums)
        answers = []
        for i in range(length):
            target = -nums[i]
            d = {}
            for j in range(i+1, length):
                if target-nums[j] in d:
                    ans = sorted([nums[i], target-nums[j], nums[j]])
                    if ans not in answers:
                        answers.append(ans)
                d[nums[j]] = True
     
        return answers
