# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])

        odd_level = False

        while q:
            if odd_level:
                lev_len = len(q)
                for i in range(lev_len//2):
                    q[i].val, q[lev_len-i-1].val = q[lev_len-i-1].val, q[i].val
            lev_len = len(q)
            for i in range(lev_len):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
        
            odd_level = not odd_level
    
        return root