class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end >-1 and s[end] == " ":
            end -= 1
        reach = end
        while reach >-1 and s[reach] != " ":
            reach -= 1
        
        return end - reach