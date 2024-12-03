class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        prev = 0
        ans = []

        for ind in spaces:
            ans.append(s[prev:ind])
            prev = ind
        ans.append(s[prev:])
        
        return " ".join(ans)