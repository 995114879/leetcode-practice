from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for k in range(2, len(nums)):
            c = nums[k]
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > c:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans


print(Solution().triangleNumber([2,2,3,4]))
