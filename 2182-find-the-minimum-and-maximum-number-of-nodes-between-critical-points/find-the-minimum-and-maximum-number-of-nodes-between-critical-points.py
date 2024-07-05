# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        mi = sys.maxsize

        if not head.next or not head.next.next:
            return [-1, -1]

        prev = head
        curr = head.next 
        next = head.next.next

        ptr = 1

        i1 = None
        i2 = None

        while next:
            if prev.val > curr.val < next.val or prev.val < curr.val > next.val:
                if i1 is None:
                    i1 = ptr
                elif i2 is None:
                    i2 = ptr
                    mi = min(mi, i2-i1)
                else:
                    mi = min(mi, ptr-i2)
                    i2 = ptr
            ptr += 1
            prev, curr, next = curr, next, next.next

        if i2 is None:
            return [-1, -1]

        ma = i2 - i1
        
        return [mi, ma]


