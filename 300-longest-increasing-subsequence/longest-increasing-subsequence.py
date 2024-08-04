from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for i in nums:
            if len(sub) == 0 or sub[-1] < i:
                sub.append(i)
            else:
                ind = bisect_left(sub, i)
                sub[ind] = i
        
        return len(sub)
