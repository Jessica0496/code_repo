from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        diff = []
        n = len(arr)
        for i in range(n):
            diff.append(arr[i] - i)
        ret = 0
        left = 0
        for i in diff:
            left += i
            if left == 0:
                ret += 1
        return ret
s = Solution()
print('4', s.maxChunksToSorted(arr = [1,0,2,3,4]))
print('1', s.maxChunksToSorted(arr = [4,3,2,1,0]))