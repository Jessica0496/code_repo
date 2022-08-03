class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ret = s
            for i in range(len(s) - 1):
                s = s[1:] + s[0]
                ret = min(ret, s)
            return ret
        else:
            return ''.join(sorted(s))
s = Solution()
print('acb', s.orderlyQueue("cba", 1))
print('aaabc', s.orderlyQueue("baaca", 3))