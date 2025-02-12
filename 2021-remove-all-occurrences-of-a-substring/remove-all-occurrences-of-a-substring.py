class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n, m = len(s), len(part)

        for i in range(n):
            stack.append(s[i])

            while len(stack) >= m and "".join(stack[len(stack)-m:]) == part:
                for _ in range(m):
                    stack.pop()
        return "".join(stack)
        

        