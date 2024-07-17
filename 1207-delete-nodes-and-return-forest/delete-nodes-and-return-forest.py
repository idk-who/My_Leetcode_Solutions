# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_del = set(to_delete)
        deleted_nodes = []
        def helper(root, to_del, roots):
            if root is None:
                return None
            
            root.left = helper(root.left, to_del, roots)
            root.right = helper(root.right, to_del, roots)
            
            if root.val in to_del:
                if root.left:
                    roots.append(root.left)
                if root.right:
                    roots.append(root.right)
                return None

            return root
        
        helper(root, to_del, deleted_nodes)
        
        # ans = []
        # for node in deleted_nodes:
        #     if node.left:
        #         ans.append(node.left)
        #     if node.right:
        #         ans.append(node.right)

        if root.val not in to_del:
            deleted_nodes.append(root)
        
        return deleted_nodes