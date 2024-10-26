# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        d = dict()
        d[None] = 0
        def rec(root):
            if not root:
                return 0
            ma = max(
                rec(root.left),
                rec(root.right)
            )

            d[root] = ma
            
            return ma + 1

        rec(root)

        ad = dict()
        def rec2(node, depth, ma):
            if not node:
                return 0
            l = rec2(node.left, depth+1, max(ma, depth+1 + d[node.right]))
            r = rec2(node.right, depth+1, max(ma, depth+1 + d[node.left]))
            
            if node.left:
                ad[node.left.val] = max(ma, r + depth)
            if node.right:
                ad[node.right.val] = max(ma, l + depth)
            
            return 1 + max(l, r)
        
        rec2(root, 0, 0)

        # print(ad)
        ans = []

        for q in queries:
            ans.append(ad[q])
        return ans