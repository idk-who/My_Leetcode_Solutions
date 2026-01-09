from bisect import bisect_left
from typing import List

class Solution:
    @staticmethod
    def num_lt(lists: List[List[int]], enabled: int, guess: int) -> int:
        result = 0
        for i in range(len(lists)):
            if (enabled >> i) & 1:
                # count elements < guess in lists[i]
                result += bisect_left(lists[i], guess)
        return result

    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)

        # collect all numbers
        all_nums = []
        for lst in lists:
            all_nums.extend(lst)
        all_nums.sort()

        # subsets[subset] = (length, median)
        subsets = [(0, 0)]

        for subset in range(1, 1 << n):
            # total length of selected lists
            result_len = 0
            for i in range(n):
                if (subset >> i) & 1:
                    result_len += len(lists[i])

            median_lt = (result_len - 1) // 2

            # binary search median
            low, high = 0, len(all_nums) - 1
            actual_median = -1

            while low <= high:
                mid = (low + high) // 2
                num = all_nums[mid]
                num_lt = self.num_lt(lists, subset, num)

                if num_lt <= median_lt:
                    actual_median = num
                    low = mid + 1
                else:
                    high = mid - 1

            subsets.append((result_len, actual_median))

        # DP over subsets
        INF = 10**30
        dp = [INF] * (1 << n)

        for subset in range(1 << n):
            if bin(subset).count("1") <= 1:
                dp[subset] = 0
            else:
                a = (subset - 1) & subset
                while a > 0:
                    b = subset ^ a
                    a_len, a_med = subsets[a]
                    b_len, b_med = subsets[b]
                    cost = a_len + b_len + abs(a_med - b_med)
                    dp[subset] = min(dp[subset], dp[a] + dp[b] + cost)
                    a = (a - 1) & subset

        return dp[(1 << n) - 1]
