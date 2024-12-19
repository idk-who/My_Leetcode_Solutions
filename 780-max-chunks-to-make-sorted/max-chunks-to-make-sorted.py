class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        
        for i in arr:
            if not stack or i >= stack[-1]:
                stack.append(i)
            else:
                ma = stack[-1]
                while stack and i < stack[-1]:
                    stack.pop()
                stack.append(ma)

        return len(stack)


