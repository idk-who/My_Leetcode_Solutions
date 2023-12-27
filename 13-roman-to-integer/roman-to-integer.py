class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        l = list(s[::-1])
        l = list(map(lambda x: dic[x], l))

        ans = l[0]
        for i in range(1,len(l)):
            if l[i]>=l[i-1]:
                ans+=l[i]
            else:
                ans-=l[i]
        return ans