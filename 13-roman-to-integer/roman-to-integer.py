class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I' :  1,
            'V' :  5,
            'X' :  10,
            'L' :  50,
            'C' :  100,
            'D' :  500,
            'M' :  1000
        }
        ns = 0
        N = len(s)
        idx = 0
        while idx < N:
            if idx+1 < N and mp[s[idx]] < mp[s[idx+1]]:
                ns += (mp[s[idx+1]] - mp[s[idx]])
                idx += 2
            else:
                ns += (mp[s[idx]])
                idx += 1
        return ns
        
