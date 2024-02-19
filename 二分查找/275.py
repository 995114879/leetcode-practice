
"""
275. H 指数 II
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数，citations 已经按照 升序排列 。计算并返回该研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （n 篇论文中）至少 有 h 篇论文分别被引用了至少 h 次。

请你设计并实现对数时间复杂度的算法解决此问题。
"""
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if citations[-mid] >= mid:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
print(Solution().hIndex([0,1,3,5,6,9,10,20]))