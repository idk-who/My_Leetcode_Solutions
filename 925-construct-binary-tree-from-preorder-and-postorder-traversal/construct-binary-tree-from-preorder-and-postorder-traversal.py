# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = {postorder[i]:i for i in range(len(postorder))}
        # print(d)
        ptr = [0, 0] # [pre, post]
        def rec(pre, post, parent_d):
            # print(ptr, parent_d)
            if ptr[0] == len(pre):
                return None
            if pre[ptr[0]] == post[ptr[1]]:
                root = TreeNode(pre[ptr[0]])
                ptr[0] += 1
                ptr[1] += 1
                return root
            if d[pre[ptr[0]]] < parent_d:
                new_parent_d = d[pre[ptr[0]]]
                root = TreeNode(pre[ptr[0]])
                ptr[0] += 1
                root.left = rec(pre, post, new_parent_d)
                root.right = rec(pre, post, new_parent_d)
                ptr[1] += 1

                return root
        
        return rec(preorder, postorder, float('inf'))