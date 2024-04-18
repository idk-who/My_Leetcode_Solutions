# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False)]

        total = 0

        while stack:
            node, isLeft = stack.pop()

            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, True))
            if node.left == None and node.right == None and isLeft:
                total += node.val

        return total

