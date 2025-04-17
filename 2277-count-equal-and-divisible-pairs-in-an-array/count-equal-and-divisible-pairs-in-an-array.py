class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0

        for j in range(n):
            for i in range(j):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    cnt += 1
        
        return cnt