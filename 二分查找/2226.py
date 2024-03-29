"""
2226. 每个小孩最多能分到多少糖果
给你一个 下标从 0 开始 的整数数组 candies 。数组中的每个元素表示大小为 candies[i] 的一堆糖果。你可以将每堆糖果分成任意数量的 子堆 ，但 无法 再将两堆合并到一起。

另给你一个整数 k 。你需要将这些糖果分配给 k 个小孩，使每个小孩分到 相同 数量的糖果。每个小孩可以拿走 至多一堆 糖果，有些糖果可能会不被分配。

返回每个小孩可以拿走的 最大糖果数目 。
"""
from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 0
        right = sum(candies) // k
        while left < right:
            mid = (left + right + 1) // 2
            total = sum(x // mid for x in candies)
            if total >= k:
                left = mid
            else:
                right = mid - 1
        return left

print(Solution().maximumCandies([1], 1))
