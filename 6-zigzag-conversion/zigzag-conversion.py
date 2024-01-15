class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        diff1 = (numRows-2)*2+2
        diff2 = 0
        ans = [] 
        for i in range(numRows):
            start = i 
            end  = len(s)
            while start<end:
                if diff1>0:
                    ans.append(s[start])
                    start+=diff1
                if start>=end:
                    break 
                if diff2>0:
                    ans.append(s[start])
                    start+=diff2
            diff1 -= 2
            diff2 += 2

        return ''.join(ans)