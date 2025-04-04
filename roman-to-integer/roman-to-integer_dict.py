class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 
             'C':100, 'D':500, 'M':1000}
        soln = 0

        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                soln -= d[s[i]]
            else:
                soln += d[s[i]]
        return soln+d[s[-1]]
