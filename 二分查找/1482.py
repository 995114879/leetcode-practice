from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        def check(mid):
            i = j = 0
            for day in bloomDay:
                if (day - 1) // mid + 1 == 1:
                    i += 1
                    if i == k:
                        i = 0
                        j += 1
                else:
                    i = 0
            return j >= m
        left = min(bloomDay)
        right = max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left, right
print(Solution().minDays([1,1], 1, 1))