class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()
        n = len(nums[0])
        ptr = 0
        for i in range(len(nums)):
            if int(nums[i], 2) != ptr:
                return bin(i)[2:].rjust(n, '0')
            ptr += 1
        return bin(ptr)[2:].rjust(n, '0')