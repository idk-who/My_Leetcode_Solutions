# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root]) 

        def count_swaps():
            cnt = 0
            org = sorted([(i.val, ind) for ind, i in enumerate(q)])
            ptr = 0
            while ptr < len(org):
                if org[ptr][1] == ptr:
                    ptr += 1
                else:
                    cnt += 1
                    ind = org[ptr][1]
                    org[ptr], org[ind] = org[ind], org[ptr]
            
            return cnt

        ans = 0
        while q:
            ans += count_swaps()

            for _ in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        
        return ans
