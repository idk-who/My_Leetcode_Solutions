"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def clone(node, created):
            if node.val in created:
                return created[node.val]

            copy = Node(node.val)
            created[node.val] = copy

            for i in node.neighbors:
                copy.neighbors.append(clone(i, created))
            return copy

        created = dict()
        return clone(node, created) if node else None