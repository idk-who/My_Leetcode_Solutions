class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height_freq = [0]*101

        for i in heights:
            height_freq[i] += 1
        
        ans = 0
        freqptr = 0
        for i in heights:
            while height_freq[freqptr] == 0: freqptr += 1
            if i != freqptr:
                ans += 1
            height_freq[freqptr] -= 1
        
        return ans