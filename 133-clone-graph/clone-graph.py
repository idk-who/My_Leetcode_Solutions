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
        created = dict()
        def clone(node, created):
            if node is None:
                return None
            if node.val in created:
                return created[node.val]
            new_node = Node(node.val)
            created[node.val] = new_node
            for i in node.neighbors:
                new_node.neighbors.append(clone(i, created))
            return new_node

        return clone(node, created)