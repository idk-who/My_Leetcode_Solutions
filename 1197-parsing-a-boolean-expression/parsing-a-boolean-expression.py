class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        
        def rec(i):
            if exp[i] == 't':
                return True, i + 1
            if exp[i] == 'f':
                return False, i + 1

            if exp[i] == '&':
                op = lambda x, y: x and y
            elif exp[i] == '|':
                op = lambda x, y: x or y
            else:
                ans, ptr = rec(i+2)
                return ((not ans), ptr + 1)
            
            ptr = i + 1
            ans = None
            while exp[ptr] != ')':
                ev, ptr = rec(ptr+1)

                if ans is None:
                    ans = ev
                else:
                    ans = op(ans, ev)

            return ans, ptr + 1

        ans, j = rec(0)
        return ans
