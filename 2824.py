from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-1):
            fast = i + 1
            while fast < n and nums[i] + nums[fast] < target:
                ans += 1
                fast += 1
        return ans
    
# print(Solution().countPairs([-1,1,2,3,1], 2))
# print(Solution().countPairs([-6,2,5,-2,-7,-1,3], -2))
print(Solution().countPairs([6,-1,7,4,2,3], 8))