from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if mid < n - 1 and nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]
    
print(Solution().singleNonDuplicate([3,3,7,7,10,11,11]))