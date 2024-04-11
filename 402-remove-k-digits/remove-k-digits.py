class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for i in num:
            while k > 0 and len(stack) > 0 and stack[-1]>i: 
                stack.pop()
                k -= 1
            stack.append(i) 
        if k > 0: stack = stack[:-k]
        
        temp = True
        ans = []
        for i in stack:
            if temp and i == '0':
                continue
            temp = False
            ans.append(i)

        if len(ans) == 0: ans.append('0')

        return "".join(ans)