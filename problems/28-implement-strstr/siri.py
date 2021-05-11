class Solution:
    def strStr(self, haystack: str, needle: str):
        if needle == '':
            return 0
        for i in range(len(haystack) - len(needle)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
