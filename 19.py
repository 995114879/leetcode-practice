# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def t1(head, n):
    dummy = ListNode(next=head)
    right = dummy
    for _ in range(n):
        right = right.next
    left = dummy
    while right.next:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        print(length)
        cur = dummy
        for _ in range(length-n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next


lists = []
for i in range(5):
    lists.append(ListNode(i))
for i in range(4):
    lists[i].next = lists[i+1]
head = lists[0]




s = Solution()
s.removeNthFromEnd(head, 5)
