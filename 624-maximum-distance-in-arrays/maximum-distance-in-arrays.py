from heapq import heappush, heappop
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mi = float("inf")
        ma = float("-inf")
        res = 0

        for arr in arrays:
            res = max(
                res,
                max(
                    ma - arr[0],
                    arr[-1] - mi
                )
            )
            mi = min(mi, arr[0])
            ma = max(ma, arr[-1])
        
        return res
            