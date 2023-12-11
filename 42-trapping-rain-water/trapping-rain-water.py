class Solution:
    def trap(self, height: List[int]) -> int:
        max_arr = [0]*len(height)
        max_ele = 0
        
        for i in range(len(height)):
            max_arr[i] = max_ele
            if max_ele < height[i]:
                max_ele = height[i]

        max_ele = 0
        for i in range(len(height)-1, -1, -1):
            max_arr[i] = min(max_arr[i], max_ele)
            if max_ele < height[i]:
                max_ele = height[i]
                
        water = 0
        for i in range(len(height)):
            water += max(max_arr[i] - height[i], 0)
        
        return water