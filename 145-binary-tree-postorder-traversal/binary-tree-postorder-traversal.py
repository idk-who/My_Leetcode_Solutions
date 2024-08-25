# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def rec(root, po):
            if root is not None:
                rec(root.left, po)
                rec(root.right, po)
                po.append(root.val)
        po = []
        rec(root, po)
        return po