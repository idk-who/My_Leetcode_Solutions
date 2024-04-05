class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n):
            low = i+1
            high = n-1
            while low<high:
                temp = nums[i] + nums[low] + nums[high]
                if temp == 0:
                    ans.add(f"{nums[i]} {nums[low]} {nums[high]}")
                    low+=1
                    high-=1
                elif temp > 0:
                    high -= 1
                else:
                    low += 1
                
        ans = [[int(j) for j in i.split()] for i in ans]
        return ans
