# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, False)

    def helper(self, node, lnode):
        if node.left == None and node.right == None:
            return node.val if lnode else 0
        if node.left == None:
            return self.helper(node.right, False)
        if node.right == None:
            return self.helper(node.left, True)
        return self.helper(node.left, True) + self.helper(node.right, False)
