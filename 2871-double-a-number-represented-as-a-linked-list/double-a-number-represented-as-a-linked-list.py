# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while head:
            head.next, tail, head = tail, head, head.next
        
        carry = 0
        s = 0
        head = None
        while tail:
            s = (tail.val * 2 + carry)%10 
            carry = (tail.val * 2 + carry)//10

            tail.val = s

            tail.next, head, tail = head, tail, tail.next
        
        if carry:
            head = ListNode(carry, head)
        
        return head


