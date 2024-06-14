class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {c:ind for ind, c in enumerate(s)}
        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                while len(stack) > 0 and stack[-1] > c and last_occ[stack[-1]] > i:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)

        return "".join(stack)