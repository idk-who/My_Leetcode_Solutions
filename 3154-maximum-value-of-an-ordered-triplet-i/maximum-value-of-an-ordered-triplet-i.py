class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = diff = hi = 0
        for k in nums:
            ans = max(ans, k*diff)
            diff = max(diff, hi-k)
            hi = max(hi, k)

        return ans