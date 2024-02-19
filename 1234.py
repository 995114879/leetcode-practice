from collections import Counter
from math import inf
class Solution:
    def balancedString(self, s: str) -> int:

        cnt, m = Counter(s), len(s) // 4
        if all(cnt[x] == m for x in "QWER"):  # 已经符合要求啦
            return 0
        ans, left = inf, 0
        for right, c in enumerate(s):  # 枚举子串右端点
            cnt[c] -= 1
            while all(cnt[x] <= m for x in "QWER"):
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1  # 缩小子串
        return ans

print(Solution().balancedString("QQQW"))
