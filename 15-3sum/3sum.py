class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if nums[i]>0: break  # optimization
            if (i>0 and nums[i-1]==nums[i]): continue  # handle duplicates of num 1
            to_find = -nums[i]
            low = i+1
            high = n-1
            while low<high:
                temp = nums[low] + nums[high]
                if temp == to_find:
                    ans.append([nums[i], nums[low], nums[high]])
                    while low<high and ans[-1][1] == nums[low]: low+=1    # handling duplicates
                    while low<high and ans[-1][2] == nums[high]: high-=1  # of num 2 and 3
                elif temp > to_find:
                    high -= 1
                else:
                    low += 1
                
        return ans