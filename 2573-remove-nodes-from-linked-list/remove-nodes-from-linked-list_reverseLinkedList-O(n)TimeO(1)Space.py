# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while head:
            head.next, head, tail = tail, head.next, head

        head = tail
        max_ele = head.val
        while head.next:
            if head.next.val < max_ele:
                head.next = head.next.next
            else:
                max_ele = head.next.val
                head = head.next
        
        head = tail 
        tail = None
        while head:
            head.next, head, tail = tail, head.next, head
        
        return tail
