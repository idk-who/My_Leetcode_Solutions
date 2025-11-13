class Solution:
    def maxOperations(self, s: str) -> int:
        carry = 0
        ans = 0

        ptr = 0
        while ptr < len(s):
            while ptr < len(s) and s[ptr] == '0':
                ptr += 1
            ans += carry

            while ptr < len(s) and s[ptr] == '1':
                carry += 1
                ptr += 1
        
        return ans