from typing import List
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def exists(s, p, mid):
            li = set(removable[: mid + 1])
            i = j = 0
            n, m = len(p), len(s)
            while i < n and j < m:
                if j not in li and p[i] == s[j]:
                    i += 1
                j += 1
            return i == n
        left = 0
        right = len(removable) - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(s, p, mid):
                left = mid + 1
            else:
                right = mid - 1
        return left
print(Solution().maximumRemovals("abcacb", "ab", [3,1,0]))

from typing import List
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        ns, np, n = len(s), len(p), len(removable)
        def check(k):
            # s 中每个字符的状态
            state = [True] * ns
            for i in range(k):
                state[removable[i]] = False
            # 匹配 s_k 与 p
            j = 0
            for i in range(ns):
                if state[i] and s[i] == p[j]:
                    j += 1
                    if j == np: 
                        return True
            return False
        # 二分查找
        left = 0
        right = len(removable) - 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        return left
