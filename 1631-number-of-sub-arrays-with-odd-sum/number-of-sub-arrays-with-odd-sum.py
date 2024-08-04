class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cnt = 0
        odds = 0
        evens = 0

        for i in arr:
            if i & 1:
                evens, odds = odds, evens + 1
            else:
                evens, odds = evens + 1, odds
            
            cnt += odds
        
        return cnt % (10**9 + 7)

