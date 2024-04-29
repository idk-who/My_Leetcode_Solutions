class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for i in nums:
            xor ^= i

        n = 0
        while xor or k:
            t1 = xor & 1
            xor >>= 1
            t2 = k & 1
            k >>= 1
            if t1 != t2:
                n += 1
        
        return n
