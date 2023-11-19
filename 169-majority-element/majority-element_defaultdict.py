class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        for i,j in dic.items():
            if j > len(nums)/2:
                return i
        
