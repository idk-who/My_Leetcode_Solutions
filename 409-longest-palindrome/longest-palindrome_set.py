class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = set()

        for i in s:
            if i in odds:
                odds.remove(i)
            else:
                odds.add(i)
        
        if len(odds) == 0:
            return len(s)
        return len(s)-len(odds)+1
