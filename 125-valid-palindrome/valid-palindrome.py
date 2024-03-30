class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        return s[:len(s)//2] == s[len(s)//2 if len(s)%2==0 else len(s)//2+1:][::-1]
