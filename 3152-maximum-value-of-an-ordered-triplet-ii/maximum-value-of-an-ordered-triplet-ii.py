class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        diff, hi, ans = 0, 0, 0

        for k in nums:
            ans = max(ans, diff*k)
            diff = max(diff, hi-k)
            hi = max(hi, k)

        return ans
