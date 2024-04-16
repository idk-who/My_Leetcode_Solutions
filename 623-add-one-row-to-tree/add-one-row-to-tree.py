# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            root = TreeNode(val, root)
        else:
            self.helper(root, val, depth)
        
        return root
    
    def helper(self, root, val, depth):
        if root is None: return
        elif depth == 2:
            root.left = TreeNode(val, root.left)
            root.right = TreeNode(val, None, root.right)
        else:
            self.helper(root.left, val, depth-1)
            self.helper(root.right, val, depth-1)