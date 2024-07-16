class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def get_sums(nums):
            set_size = 2 ** len(nums)
            poss = [[] for _ in range(len(nums)+1)]
            for i in range(set_size):
                su = 0
                sz = 0
                for j in range(len(nums)):
                    if i & (1 << j):
                        su += nums[j]
                        sz += 1
                poss[sz].append(su)
            return poss

        sums_l, sums_r = get_sums(nums[:len(nums)//2]), get_sums(nums[len(nums)//2:])

        ans = float("inf")
        ts = sum(nums)
        target = sum(nums)/2
        for i in range(len(nums)//2):
            s1 = sums_l[i]
            s2 = sums_r[len(nums)//2-i]
            s2.sort()
            for n in s1:
                l = 0
                r = len(s2)-1
                t = target-n
                while l <= r:
                    m = l + (r-l)//2
                    if s2[m] == t:
                        # print(ts, n, s2[m])
                        return 0
                    elif s2[m] < t:
                        l = m + 1
                    else:
                        r = m - 1
                if l < len(s2): ans = min(ans, abs(ts-2*(n+s2[l])))
                if l-1 >= 0:    ans = min(ans, abs(ts-2*(n+s2[l-1])))
                # print(ans)

        return ans