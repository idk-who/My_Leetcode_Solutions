class Solution:
    def isPalindrome(self, s: str) -> bool:
        return [i.lower() for i in s if i.isalnum()] == [i.lower() for i in s if i.isalnum()][::-1]
