class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        locked_pos = [-1]*50
        le = -1
        ans = 0

        for i in range(len(nums)):
            for ind, bit in enumerate(reversed(bin(nums[i])[2:])):
                if bit == '1':
                    if locked_pos[ind] > le:
                        le = locked_pos[ind]
                    locked_pos[ind] = i
            
            ans = max(
                ans,
                i-le
            )
        
        return ans