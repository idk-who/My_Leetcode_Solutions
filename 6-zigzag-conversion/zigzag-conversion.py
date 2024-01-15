class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        diff1 = (numRows-2)*2+2
        diff2 = 0
        ans = [] 
        for i in range(numRows):
            start = i 
            end  = len(s)
            # print("\n\nLoop", i+1)
            while start<end:
                # print(i+1, start, "diff1", diff1)
                if diff1>0:
                    ans.append(s[start])
                    start+=diff1

                if diff2>0:
                    if start>=end:
                        break 
                    ans.append(s[start])
                    start+=diff2
            diff1 -= 2
            diff2 += 2

        # print(''.join(ans))

        return ''.join(ans)