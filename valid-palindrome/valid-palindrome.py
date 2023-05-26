class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [a for a in s.lower() if a.isalnum()]
        return s == s[::-1]