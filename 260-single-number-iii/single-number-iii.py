class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for i in nums:
            xor ^= i
        
        diff = xor & (xor-1) ^ xor

        dig1 = 0
        dig2 = 0

        for i in nums:
            if i & diff:
                dig1 ^= i
            else:
                dig2 ^= i
        
        return [dig1, dig2]