class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            a, b = 'a', 'b'
        else:
            a, b, = 'b', 'a'
            x, y = y, x

        stack = []
        ans = 0
        for c in s:
            if len(stack) > 0 and c == a and stack[-1] == b:
                stack.pop()
                ans += y
            else:
                stack.append(c)
        s = stack
        stack = []

        for c in s:
            if len(stack) > 0 and c == b and stack[-1] == a:
                stack.pop()
                ans += x
            else:
                stack.append(c)

        return ans