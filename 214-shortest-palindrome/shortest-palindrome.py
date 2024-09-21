class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev_s = s[::-1]

        for i in range(n, -1, -1):
            if s[:i] == rev_s[n-i:]:
                return rev_s[:n-i] + s 
 
