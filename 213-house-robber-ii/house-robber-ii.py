class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        def fxn(nums, lo, hi):
            one = nums[lo]
            two = max(nums[lo+1], one)

            for i in range(lo+2, hi):
                two, one = max(nums[i]+one, two), two
            
            return two
        
        ans1 = fxn(nums, 0, n-1) 
        
        ans2 = fxn(nums, 1, n) 

        return max(ans1, ans2)