from typing import List
import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hq = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                heapq.heappush(hq, -diff)
                bricks -= diff
                if bricks < 0:
                    if ladders:
                        ladders -= 1
                        bricks -= heapq.heappop(hq)
                    else:
                        return i - 1
        return len(heights) - 1


    

print(Solution().furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2))