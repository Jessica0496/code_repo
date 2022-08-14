class Solution:
    def maxScore(self, s: str) -> int:
        ret = 0
        for i in range(1, len(s)):
            ret = max(ret, s[:i].count('0') + s[i:].count('1'))
        return ret
s = Solution()
print('4', s.maxScore("01001"))
print('5', s.maxScore("011101"))
print('1', s.maxScore("00"))
print('5', s.maxScore("00111"))
print('3', s.maxScore("1111"))
