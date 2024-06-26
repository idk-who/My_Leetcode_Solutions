# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        self.createList(root, arr)
        return self.createTree(arr, 0, len(arr)-1)

    def createList(self, root, arr):
        if root.left:
            self.createList(root.left,arr)
        arr.append(root.val)
        if root.right:
            self.createList(root.right,arr)

    def createTree(self, arr, lo, hi):
        if lo > hi:
            return None
        mid = (lo+hi)//2
        return TreeNode(arr[mid], self.createTree(arr, lo, mid-1), self.createTree(arr, mid+1, hi))
