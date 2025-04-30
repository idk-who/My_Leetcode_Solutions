class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            le = 0
            while i:
                le += 1
                i //= 10
            if not le&1:
                cnt += 1
        
        return cnt