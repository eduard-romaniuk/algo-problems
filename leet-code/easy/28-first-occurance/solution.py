class Solution:
    def is_correct_substr(self, haystack: str, needle: str, start: int):
        for i in range(len(needle)):
            if haystack[start + i] != needle[i]:
                return False
        return True

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                if self.is_correct_substr(haystack, needle, i):
                    return i
        return -1
