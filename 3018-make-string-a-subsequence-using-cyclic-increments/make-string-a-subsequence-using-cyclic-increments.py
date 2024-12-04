class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def match(c1, c2):
            return c1 == c2 or chr((ord(c1)-ord('a')+1)%26 + ord('a')) == c2
        
        p1 = 0
        p2 = 0

        while p1 < len(str1) and p2 < len(str2):
            if match(str1[p1], str2[p2]):
                p2 += 1
            p1 += 1
        print(p1, p2)
        return p2 == len(str2)