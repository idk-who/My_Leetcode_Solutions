class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        n = len(candies)
        def can_allocate(num):
            children = k
            ptr = 0
            while children > 0 and ptr < n:
                children -= candies[ptr]//num
                ptr += 1
            
            return children <= 0
        
        mi = 1
        ma = max(candies)

        while mi < ma:
            mid = (mi+ma+1)//2
            if can_allocate(mid):
                mi = mid
            else:
                ma = mid - 1
        
        return mi
