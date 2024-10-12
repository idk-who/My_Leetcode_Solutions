from heapq import heappush, heappop
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 1
        h = [-1]
        # print(intervals)
        for l, r in intervals:
            prev = heappop(h)

            if l > prev:
                heappush(h, r)
            else:
                ans += 1
                heappush(h, prev)
                heappush(h, r)
            # print(h)
        
        return len(h)
