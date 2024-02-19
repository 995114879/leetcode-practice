from typing import List
from math import inf
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        ans = 0
        def check(num, com):
            money = 0
            for s, base, c in zip(stock, com, cost):
                if s < base * num:
                    money += (base * num - s) * c
                    if money > budget:
                        return False
            return True
        for com in composition:
            left = 0
            right = min(stock) + budget
            while left <= right:
                mid = (left + right) // 2
                if check(mid, com):
                    left = mid + 1
                else:
                    right = mid - 1
            ans = max(ans, right)
        return ans
print(Solution().maxNumberOfAlloys(3, 2, 15, [[1,1,1],[1,1,10]], [0,0,0], [1,2,3]))
print(Solution().maxNumberOfAlloys(3, 2, 15, [[1,1,1],[1,1,10]], [0,0,100], [1,2,3]))
print(Solution().maxNumberOfAlloys(1, 7, 48, [[1],[5],[9],[6],[4],[2],[4]], [6], [1]))
print(Solution().maxNumberOfAlloys(1, 1, 100, [[97]], [15496474], [81]))# 159757
