from typing import List
from itertools import product
from functools import lru_cache
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        @lru_cache
        def dfs(n):
            if n == 1: return ["()"]
            ans = set("(" + x + ")" for x in dfs(n - 1))
            for i in range(1, n): ans |= set(l + r for l, r in product(dfs(i), dfs(n - i)))
            return list(ans)
        return dfs(n)


        




s = Solution()

print(s.generateParenthesis(3))
