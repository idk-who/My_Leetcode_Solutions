class Solution:
    def checkValidString(self, s: str) -> bool:
        min_p = 0
        max_p = 0

        for i in s:
            if i == '(':
                min_p += 1
                max_p += 1
            elif i == '*':
                min_p = max(min_p-1, 0)
                max_p += 1
            else:
                min_p = max(min_p-1, 0)
                max_p -= 1
            if max_p < 0:
                return False
        
        return min_p == 0
