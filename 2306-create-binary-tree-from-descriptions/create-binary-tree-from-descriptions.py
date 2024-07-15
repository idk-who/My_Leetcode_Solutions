# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        for p, c, i in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(val=p)
            if c not in nodes:
                nodes[c] = TreeNode(val=c)
        parent = 0
        for k in nodes:
            parent ^= k
        for p, c, i in descriptions:
            parent ^= c
            if i:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
        
        return nodes[parent]