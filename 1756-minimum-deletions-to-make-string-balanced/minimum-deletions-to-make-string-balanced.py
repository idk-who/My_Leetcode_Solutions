class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        pre = [0]*n
        post = [0]*n

        carry = 0
        for i in range(n):
            pre[i] = carry
            if s[i] == 'b':
                carry += 1
        
        carry = 0
        for i in range(n-1, -1, -1):
            post[i] = carry
            if s[i] == 'a':
                carry += 1
        
        ans = float("inf")
        for i in range(n):
            ans = min(ans, pre[i]+post[i])
        
        return ans