# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        depth = []
        nodes = []
        dashes = 0

        ptr = 0 
        while ptr < len(traversal):
            if traversal[ptr] == '-':
                dashes += 1
                ptr += 1
            else:
                num = 0
                while ptr < len(traversal) and traversal[ptr] != '-':
                    num = num*10 + int(traversal[ptr])
                    ptr += 1
                depth.append(dashes)
                nodes.append(num)
                dashes = 0
        
        self.ptr = 0
        def rec(nodes, curr_depth):
            if self.ptr < len(nodes) and depth[self.ptr] == curr_depth:
                root = TreeNode(nodes[self.ptr])
                self.ptr += 1
                root.left = rec(nodes, curr_depth+1)
                root.right = rec(nodes, curr_depth+1)
                return root
            
        return rec(nodes, 0)
        
