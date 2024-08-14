class Solution:
    def smallestDistancePair(self, nums, k):
        def possible(guess_dist):
            i = count = 0
            j = 1
            while i < len(nums):
                while (j < len(nums)) and ((nums[j] - nums[i]) <= guess_dist):
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]

        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
