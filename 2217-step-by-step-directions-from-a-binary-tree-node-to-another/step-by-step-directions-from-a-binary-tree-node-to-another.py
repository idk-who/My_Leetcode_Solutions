# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find_path(root, val, path):
            if root == None: return False
            if root.val == val: return True

            path.append("L")
            if find_path(root.left, val, path): return True
            path.pop()

            path.append("R")
            if find_path(root.right, val, path): return True
            path.pop()

            return False
        
        lPath = []
        find_path(root, startValue, lPath)

        rPath = []
        find_path(root, destValue, rPath)

        ptr = 0
        while ptr < len(lPath) and ptr < len(rPath) and lPath[ptr] == rPath[ptr]:
            ptr += 1

        return "U"*(len(lPath)-ptr)+"".join(rPath[ptr:]) 