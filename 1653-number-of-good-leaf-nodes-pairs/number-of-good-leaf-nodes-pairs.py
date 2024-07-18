# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def rec(root, distance) -> (int, list):
            if root is None:
                return 0, []
            if root.left is None and root.right is None:
                return 0, [1]

            ln, ll = rec(root.left, distance)
            rn, rl = rec(root.right, distance) 
            n = ln + rn
            for i in ll:
                for j in rl:
                    if i+j <= distance:
                        n += 1
            l = []
            for i in ll:
                if i+1 < distance:
                    l.append(i+1)
            for i in rl:
                if i+1 < distance:
                    l.append(i+1)
            return n, l
        
        n, _ = rec(root, distance)
    
        return n