class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def helper(bound):
            cnt = 0
            lo = 0
            hi = len(nums) - 1

            while lo < hi:
                if nums[lo] + nums[hi] <= bound:
                    cnt += hi - lo
                    lo += 1
                else:
                    hi -= 1
            
            return cnt
        
        return helper(upper) - helper(lower-1)
