
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        need = len(needle)
        if need == 0:
            return 0
        for i in range(len(haystack) - need + 1):
            if haystack[i:i + need] == needle:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("hello", "ll"))
    print(s.strStr("aaaaa", "bba"))