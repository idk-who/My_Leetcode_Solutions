class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def check(nu):
            ptr = 0 
            temp_k = k
            while ptr < n:
                if nums[ptr] <= nu:
                    temp_k -= 1
                    ptr += 2
                else:
                    ptr += 1
            
            return temp_k <= 0
        
        lo = min(nums)
        hi = max(nums)
        ans = float('inf')
        while lo <= hi:
            mid = (lo+hi)//2

            if check(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans