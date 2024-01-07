class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = len(strs[0])
        for s in strs:
            if len(s)<minlen:
                minlen = len(s)
            
        for i in range(minlen):
            temp = strs[0][i]
            for s in strs:
                if s[i]!=temp:
                    return strs[0][:i]
                
        return strs[0][:minlen]

