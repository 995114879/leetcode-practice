from typing import List
from math import inf
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def juge(weights, mid):
            day = 1
            t = 0
            for w in weights:
                t += w
                if t > mid:
                    day += 1
                    t = w
            return day <= days
        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            if juge(weights, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

        
    
print(Solution().shipWithinDays([1,2,3,1,1], 4))