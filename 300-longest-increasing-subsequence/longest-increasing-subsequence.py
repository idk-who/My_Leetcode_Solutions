from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        seq = []

        for i in range(n):
            if len(seq) == 0 or seq[-1] < nums[i]:
                seq.append(nums[i])
            else:
                ind = bisect_left(seq, nums[i])
                seq[ind] = nums[i]

        return len(seq)

        







