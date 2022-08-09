from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ret = 1
        if ret < 0:
            ret = 1 - ret

        start = ret
        for n in nums:
            start += n
            if start < 1:
                diff = 1 - start
                ret += diff
                start = 1
        return ret

s = Solution()
print('5', s.minStartValue([-3,2,-3,4,2]))
print('5', s.minStartValue([1,-2,-3]))
print('1', s.minStartValue([1,2]))
print('1', s.minStartValue([2,3,5,-5,-1]))