from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours = sum((x - 1) // mid + 1 for x in piles)
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left
print(Solution().minEatingSpeed([30,11,23,4,20], 6))