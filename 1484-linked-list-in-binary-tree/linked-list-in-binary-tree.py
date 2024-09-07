# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def rec2(root, head):
            if head is None: return True
            if root is None: return False
            
            if root.val == head.val:
                return rec2(root.left, head.next) or rec2(root.right, head.next)
            else:
                return False

        def rec(root, head):
            if head is None: return True
            if root is None: return False

            return rec2(root, head) or rec(root.left, head) or rec(root.right, head)

        return rec(root, head)