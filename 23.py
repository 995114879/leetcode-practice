from typing import List, Optional
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        heap = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        while heap:
            val, i = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return dummy.next
            

s = Solution()
lists = [[1,4,5],[1,3,4],[2,6]]
res = s.mergeKLists(lists)
print(res)