# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        d = defaultdict(int)

        def rec(root, depth):
            if root:
                d[depth] += root.val
                rec(root.left, depth+1)
                rec(root.right, depth+1)
        
        rec(root, 0)
        if len(d) < k:
            return -1
        return sorted(d.values(), reverse=True)[k-1]