from typing import List
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [0] * (m*n)
        for i, j in indices:
            for k in range(n):
                matrix[i * n + k] += 1
            for k in range(m):
                matrix[k * n + j] += 1
        ret = 0
        for i in matrix:
            if i % 2 == 1:
                ret += 1
        return ret
s = Solution()
print('6', s.oddCells(m=2, n=3, indices=[[0,1],[1,1]]))
print('0', s.oddCells(m = 2, n = 2, indices = [[1,1],[0,0]]))