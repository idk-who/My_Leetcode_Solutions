class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        m = (r-l)*min(height[l], height[r])

        while l < r:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            m = max(m, (r-l)*min(height[l], height[r]))
            
        return m
