# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(left, right, odd=True):
            if left:
                if odd:
                    left.val, right.val = right.val, left.val

                rec(left.left, right.right, not odd)
                rec(left.right, right.left, not odd)

        rec(root.left, root.right, True)
        return root
