from typing import List

def lower_bound(nums, target):#()
    left = -1
    right = len(nums)
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    return right
def lower_bound1(nums, target): #[)
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right

def lower_bound2(nums, target): #[}
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid + 1
    return right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        print(lower_bound(nums,9))
        print(target + 1)
        end = lower_bound(nums, target + 1) - 1
        return [start, end]
    

s = Solution()
print(s.searchRange([5,7,7,8,8,10,10], 8))