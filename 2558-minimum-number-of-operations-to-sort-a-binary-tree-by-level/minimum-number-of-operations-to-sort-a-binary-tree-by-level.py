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
            org = [i.val for i in q]
            pos = {val: ind for ind, val in enumerate(org)}
            srt = sorted(org)
            ptr = 0
            while ptr < len(org):
                if org[ptr] != srt[ptr]:
                    cnt += 1
                    srt_ind = pos[srt[ptr]]
                    pos[org[ptr]] = srt_ind
                    org[srt_ind] = org[ptr] 

                    # The blow also works (but a bit unoptimal)
                    # srt_ind = pos[srt[ptr]]
                    # pos[org[ptr]] = srt_ind
                    # pos[org[srt_ind]] = ptr
                    # org[ptr], org[srt_ind] = org[srt_ind], org[ptr]
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
