# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dp = []
        return self.helper(root)

    def helper(self, root):
        self.dp.append(str(root.val))
        if root.left == None and root.right == None:
            ans = int("".join(self.dp))
        elif root.left is None:
            ans = self.helper(root.right)
        elif root.right is None:
            ans = self.helper(root.left)
        else:
            ans = self.helper(root.left) + self.helper(root.right)
        self.dp.pop()
        
        return ans