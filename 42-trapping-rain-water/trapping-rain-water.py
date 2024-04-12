class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [0]*n
        m = -1
        for i in range(n):
            if height[i]>m: m = height[i]
            max_l[i] = m

        max_r = [0]*n
        m = -1
        for i in range(n-1, -1, -1):
            if height[i]>m: m = height[i]
            max_r[i] = m
        
        ans = 0
        for i in range(n):
            ans += min(max_l[i], max_r[i]) - height[i]

        return ans