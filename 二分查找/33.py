from typing import List
def s1(nums, target):
    left = -1
    right = len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < nums[-1]:
            right = mid
        else:
            left = mid
    if nums[-1] >= target:
        l = right - 1
        r = len(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
    else:
        l = -1
        r = right
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
    if r == len(nums) or nums[r] != target:
        return -1
    return r
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i):
            end = nums[-1]
            if nums[i] > end:
                return target > end and nums[i] >= target
            else:
                return target > end or nums[i] >= target
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid
        if right == len(nums) or nums[right] != target:
            return -1
        return right
        

s = Solution()
print(s.search([1,3], 3))
