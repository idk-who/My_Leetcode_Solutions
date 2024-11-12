class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        ma = 0
        for i, (p, b) in enumerate(items):
            ma = max(ma, b)
            items[i][1] = ma
        
        ans = []
        for q in queries:
            ma = 0
            
            lo = 0
            hi = len(items) - 1
            mi = 0
            while lo <= hi:
                mi = (lo+hi)//2
                if items[mi][0] > q:
                    hi = mi - 1
                else:
                    ma = max(ma, items[mi][1])
                    lo = mi + 1
            
            ans.append(ma)
    
        return ans
        
