# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, False)])

        total = 0

        while queue:
            node, isLeft = queue.popleft()

            if node.right:
                queue.append((node.right, False))
            if node.left:
                queue.append((node.left, True))
            if node.left == None and node.right == None and isLeft:
                total += node.val

        return total

