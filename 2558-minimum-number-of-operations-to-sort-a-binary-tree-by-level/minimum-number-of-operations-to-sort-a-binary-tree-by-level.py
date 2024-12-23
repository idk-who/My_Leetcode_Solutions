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
            org = [[i.val, ind] for ind, i in enumerate(q)]
            org.sort()
            
            ptr = 0
            while ptr < len(org):
                if org[ptr][1] != ptr and org[ptr][0] != -1:
                    cycle_ln = 0

                    while org[ptr][0] != -1:
                        org[ptr][0] = -1
                        ptr = org[ptr][1]
                        cycle_ln += 1
                    cnt += cycle_ln - 1
                    
                ptr += 1
            
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
