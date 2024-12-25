# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largest_vals = []

        def rec(root, depth):
            if root:
                if len(largest_vals) < depth:
                    largest_vals.append(root.val)
                else:
                    largest_vals[depth-1] = max(
                        largest_vals[depth-1],
                        root.val
                    )
                rec(root.left, depth+1)
                rec(root.right, depth+1)
        
        rec(root, 1)

        return largest_vals