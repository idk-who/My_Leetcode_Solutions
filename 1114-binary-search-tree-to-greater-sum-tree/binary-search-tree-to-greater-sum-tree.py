# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.setGetKey(root, 0)
        return root
    
    def setGetKey(self, root, total):
        if root.right:
            total = self.setGetKey(root.right, total)

        total += root.val
        root.val = total

        if root.left:
            total = self.setGetKey(root.left, total)

        return total