class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maximixzed = (1<<maximumBit) - 1

        xor = 0
        for i in nums: 
            xor ^= i

        ans = []
        for i in reversed(nums):
            ans.append(xor^maximixzed)

            xor ^= i
        
        return ans