class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odds = 0
        evens = 0

        ans = 0

        for i in arr:
            if i&1:
                new_odds = evens + 1
                new_evens = odds
            else:
                new_odds = odds
                new_evens = evens + 1
            odds = new_odds % (10**9+7)
            evens = new_evens % (10**9+7)
            ans = (ans + odds) % (10**9+7)
            # print(odds, evens)

        return ans 