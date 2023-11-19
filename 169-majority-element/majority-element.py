class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1
        for i,j in dic.items():
            if j > len(nums)/2:
                return i
        