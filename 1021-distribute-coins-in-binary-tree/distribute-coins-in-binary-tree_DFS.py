# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        self.DFS(root)
        return self.moves

    def DFS(self, root):
        if root == None:
            return 0

        left = self.DFS(root.left)
        right = self.DFS(root.right)
        self.moves += abs(left) + abs(right)

        return root.val + left + right - 1

        
