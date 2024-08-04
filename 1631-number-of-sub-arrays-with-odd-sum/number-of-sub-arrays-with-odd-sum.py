class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cnt = 0
        odds = 0
        evens = 0

        for i in arr:
            if i & 1:
                evens, odds = odds, evens + 1
            else:
                evens = evens + 1
            
            cnt = (cnt + odds) % (10**9 + 7)
        
        return cnt

