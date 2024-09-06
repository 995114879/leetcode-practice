class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        while s*s <= x:
            s += 1
            if s*s > x:
                return s - 1