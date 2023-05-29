class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        for i in range(min(map(len, strs))):
            if all([j[i] == strs[0][i] for j in strs]):
                out += strs[0][i]
            else:
                break
        return out