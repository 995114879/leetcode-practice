from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            # 要交换的两个节点
            first = head
            second = head.next
            
            # 交换节点位置
            prev.next = second
            first.next = second.next
            second.next = first

            # 更新指针
            prev = first
            head = first.next
        return dummy.next
    
li = [1, 2, 3, 4]
dummy = ListNode(0)
current = dummy
for i in li:
    current.next = ListNode(i)
    current = current.next

# 调用函数
s = Solution()
res = s.swapPairs(dummy.next)

# 打印链表的值
result_list = []
current = res
while current:
    result_list.append(current.val)
    current = current.next

print(result_list)