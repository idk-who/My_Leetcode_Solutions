# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        org_head = head

        while head.next:
            n1 = head.val
            n2 = head.next.val
            head.next = ListNode(gcd(n1, n2), head.next)
            head = head.next.next
        
        return org_head
