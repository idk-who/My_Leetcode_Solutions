class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i in num:
            while k > 0 and len(stack) > 0 and stack[-1]>i: 
                stack.pop()
                k -= 1
            stack.append(i) 

        while k > 0 and len(stack)>0: 
            stack.pop()
            k -= 1

        start = 0
        while start<len(stack) and stack[start]=='0': start += 1
        stack = stack[start:]

        if len(stack) == 0: stack.append('0')
        
        ans = "".join(stack)

        return ans