from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-3):
            x = nums[i]
            if i and x == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                y = nums[j]
                if j > i + 1 and y == nums[j-1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    s = x + y + nums[left] + nums[right]
                    if s > target:
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        ans.append([x,y,nums[left],nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
        return ans