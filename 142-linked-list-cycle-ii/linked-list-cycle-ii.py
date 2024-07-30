# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = set()
        ind = 0
        while head:
            if head in d:
                return head
            d.add(head)
            
            ind += 1
            head = head.next

        return None