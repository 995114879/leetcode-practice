from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0 = dummy
        t = dummy.next
        count = 0
        while t:
            count += 1
            t = t.next
        cur = p0.next
        pre = None
        while k <= count:
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
            count -= k
        return dummy.next


        


        