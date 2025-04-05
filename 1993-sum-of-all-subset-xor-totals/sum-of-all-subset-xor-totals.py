class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        xor_sum = 0
        for b in range(2**n):
            xor = 0
            for i in range(n):
                if b&(1<<i):
                    xor ^= nums[i]
            xor_sum += xor
        
        return xor_sum