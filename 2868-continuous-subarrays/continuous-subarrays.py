from heapq import heappush, heappop
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        mi = []
        ma = []
        
        l = 0
        for ind, i in enumerate(nums):
            heappush(mi, (i, ind))
            heappush(ma, (-i, ind))

            min_num = mi[0][0]
            max_num = -ma[0][0]

            while max_num - min_num > 2:
                l += 1
                while mi[0][1] < l:
                    heappop(mi)
                while ma[0][1] < l:
                    heappop(ma)
                min_num = mi[0][0]
                max_num = -ma[0][0]
            
            ans += ind-l+1
        
        return ans
                
                

