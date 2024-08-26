"""
给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。

整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。

返回被除数 dividend 除以除数 divisor 得到的 商 。
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 处理溢出情况
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # 确定结果的符号
        negative = (dividend < 0) != (divisor < 0)

        # 将被除数和除数转为正数
        dividend, divisor = abs(dividend), abs(divisor)

        # 初始化商
        quotient = 0
        
        # 通过减法和位移操作计算商
        while dividend >= divisor:
            # 计算可以减去的最大倍数
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            # 减去最大倍数对应的除数部分
            dividend -= temp
            quotient += multiple

        # 如果结果是负数，取反
        if negative:
            quotient = -quotient

        # 返回截断后的结果
        return min(max(-2**31, quotient), 2**31 - 1)

res = Solution().divide(-147258369, -1)
print(res)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        
        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0
        
        # 一般情况，使用二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        # 快速乘
        def quickAdd(y: int, z: int, x: int) -> bool:
            # x 和 y 是负数，z 是正数
            # 需要判断 z * y >= x 是否成立
            result, add = 0, y
            while z > 0:
                if (z & 1) == 1:
                    # 需要保证 result + add >= x
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    # 需要保证 add + add >= x
                    if add < x - add:
                        return False
                    add += add
                # 不能使用除法
                z >>= 1
            return True
        
        left, right, ans = 1, INT_MAX, 0
        while left <= right:
            # 注意溢出，并且不能使用除法
            mid = left + ((right - left) >> 1)
            check = quickAdd(divisor, mid, dividend)
            if check:
                ans = mid
                # 注意溢出
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1

        return -ans if rev else ans


