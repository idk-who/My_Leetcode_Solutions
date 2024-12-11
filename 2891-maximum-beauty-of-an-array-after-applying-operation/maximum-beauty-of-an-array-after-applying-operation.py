class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        ma = 1

        def find_l(nums, n):
            l = 0
            r = len(nums)-1

            while l <= r:
                m = (l+r)//2
                if nums[m] >= n:
                    r = m - 1
                else:
                    l = m + 1

            return r

        def find_r(nums, n):
            l = 0
            r = len(nums)-1

            while l <= r:
                m = (l+r)//2
                if nums[m] > n:
                    r = m - 1
                else:
                    l = m + 1

            return l

        for i in range(min(nums), max(nums)+1):
            l = find_l(nums, i-k)
            r = find_r(nums, i+k) - 1
            # print(i, l, r)
            ma = max(ma, r-l)
        
        return ma