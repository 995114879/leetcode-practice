from typing import List
from math import inf
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1
        ans = inf
        left = 1
        right = max(dist) * 100
        while left <= right:
            mid = (left + right) // 2
            times = sum((x-1) // mid + 1 for x in dist[:-1])
            times += dist[-1] / mid
            if times <= hour:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans
print(Solution().minSpeedOnTime([1,1], 1.0))