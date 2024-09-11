"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = Node(-1)
        
        new_ptr = new_head
        old_ptr = head
        store = dict()

        while old_ptr:
            
            if old_ptr in store:
                new_node = store[old_ptr]
            else:
                new_node = Node(
                    old_ptr.val,
                )
                store[old_ptr] = new_node

            new_ptr.next = new_node

            if old_ptr.random == None:
                random = None
            elif old_ptr.random in store:
                random = store[old_ptr.random]
            else:
                random = Node(
                    old_ptr.random.val
                )
                store[old_ptr.random] = random
            new_ptr.next.random = random

            old_ptr = old_ptr.next
            new_ptr = new_ptr.next
        
        return new_head.next