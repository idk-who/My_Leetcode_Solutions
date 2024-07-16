class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def get_sums(nums):
            set_size = 2 ** len(nums)
            for i in range(set_size):
                su = 0
                for j in range(len(nums)):
                    if i & (1 << j):
                        su += nums[j]
                yield su
        
        sums_left = sorted(get_sums(nums[:len(nums)//2]))
        ans = float("inf")
        for i in get_sums(nums[len(nums)//2:]):

            l = 0
            r = len(sums_left)
            target = goal - i
            while l < r:
                m = l + (r-l)//2
                if sums_left[m] == target:
                    return 0
                elif sums_left[m] < target:
                    l = m + 1
                else:
                    r = m
            
            ans = min(ans, abs(goal-sums_left[m]-i))
            ans = min(ans, abs(goal-sums_left[m-1]-i))
            if m+1 < len(sums_left): ans = min(ans, abs(goal-sums_left[m+1]-i))
        
        return ans


        

        return helper(nums, goal, 0, dict())