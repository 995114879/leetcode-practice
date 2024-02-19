from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1
        for _ in numbers:
            if numbers[first] + numbers[last] > target:
                last -= 1
            elif numbers[first] + numbers[last] < target:
                first += 1
            else:
                return [first + 1, last + 1]