# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:

        node = head
        
        while node.next:
           node.next, node = ListNode(gcd(node.val, node.next.val
                                         ), node.next), node.next
        return head