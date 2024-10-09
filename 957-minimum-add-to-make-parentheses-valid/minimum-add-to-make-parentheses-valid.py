class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        ans = 0

        for i in s:
            if i == '(':
                left += 1
            else:
                if left:
                    left -= 1
                else:
                    ans += 1
        
        return ans + left