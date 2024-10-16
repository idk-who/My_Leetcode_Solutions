from heapq import heappop, heappush
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        heappush(h, (-a, 'a'))
        heappush(h, (-b, 'b'))
        heappush(h, (-c, 'c'))
        ans = ""
        while h[0][0] < 0:
            if ans == "" or ans[-1] != h[0][1]:
                n, ele = heappop(h)
                ans += ele * min(2, -n)
                n += min(2, -n)
                heappush(h, (n, ele))
            else:
                sn, sele = heappop(h)

                if h[0][0] == 0:
                    break
                n, ele = heappop(h)
                ans += ele * min(1, -n)
                n += min(1, -n)
                heappush(h, (n, ele))

                heappush(h, (sn, sele))
        return ans