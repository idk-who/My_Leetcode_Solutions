class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref = 0
        suff = sum(nums)
        splits = 0
        for i in range(len(nums)-1):
            pref += nums[i]
            suff -= nums[i]
            if pref >= suff:
                splits += 1

        return splits