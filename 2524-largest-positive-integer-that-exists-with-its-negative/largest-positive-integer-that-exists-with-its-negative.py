class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        freq = [None]*1001

        for i in nums:
            if freq[abs(i)] is None:
                freq[abs(i)] = i
            elif freq[abs(i)] < 0 and i > 0:
                freq[abs(i)] += i
            elif freq[abs(i)] > 0 and i < 0:
                freq[abs(i)] += i
        
        for i in range(1000, -1, -1):
            if freq[i] == 0:
                return i
        
        return -1