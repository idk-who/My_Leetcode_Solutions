# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []
        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        keep = []
        m = stack[-1]
        for i in reversed(stack):
            if i >= m:
                m = i
                keep.append(m)

        dummy = ListNode(None, head)
        ans = dummy
        ptr = len(keep)-1
        while dummy.next:
            if ptr >= 0 and dummy.next.val != keep[ptr]:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
                ptr -= 1

        return ans.next