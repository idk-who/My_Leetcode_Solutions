# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode], n=0):
        self.root = root
        self.data = set()
        self.fill(root, 0)
    
    def fill(self, root, n):
        if root:
            self.data.add(n)
            self.fill(root.left, 2*n+1)
            self.fill(root.right, 2*n+2)

    def find(self, target: int) -> bool:
        return target in self.data

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)