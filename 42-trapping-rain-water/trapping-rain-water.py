class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [0]*n
        m = -1
        for i in range(n):
            if height[i]>m: m = height[i]
            max_l[i] = m
        
        ans = 0
        m = -1
        for i in range(n-1, -1, -1):
            if height[i]>m: m = height[i]
            ans += min(max_l[i], m) - height[i]

        return ans