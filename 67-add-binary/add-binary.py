class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        i = len(a)-1
        j = len(b)-1
        carry = 0
        while i >= 0 or j >= 0:
            sum = carry 
            if i>=0 and a[i] == '1' : sum += 1
            if j>=0 and b[j] == '1' : sum += 1

            carry = sum // 2
            if sum%2 == 0: res.append('0') 
            else: res.append('1')

            i -= 1
            j -= 1
        if carry == 1: res.append("1")
        
        return "".join(res[::-1])