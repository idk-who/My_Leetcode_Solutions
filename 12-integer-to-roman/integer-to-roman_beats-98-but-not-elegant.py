class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        while num >= 1000:
            ans.append('M')
            num -= 1000
        
        if num >= 900:
            ans.append('CM')
            num -= 900
        
        while num >= 500:
            ans.append('D')
            num -= 500
        
        if num >= 400:
            ans.append('CD')
            num -= 400
        
        while num >= 100:
            ans.append('C')
            num -= 100
        
        if num >= 90:
            ans.append('XC')
            num -= 90

        while num >= 50:
            ans.append('L')
            num -= 50
        
        if num >= 40:
            ans.append('XL')
            num -= 40

        while num >= 10:
            ans.append('X')
            num -= 10
        
        if num >= 9:
            ans.append('IX')
            num -= 9

        while num >= 5:
            ans.append('V')
            num -= 5
        
        if num >= 4:
            ans.append('IV')
            num -= 4

        while num >= 1:
            ans.append('I')
            num -= 1

        return "".join(ans)
