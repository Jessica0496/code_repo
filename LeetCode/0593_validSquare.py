from typing import List
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        point_list = [p1, p2, p3, p4]
        point_list.sort()
        b1_len = (point_list[0][0] - point_list[1][0]) * (point_list[0][0] - point_list[1][0]) + \
                 (point_list[0][1] - point_list[1][1]) * (point_list[0][1] - point_list[1][1])
        b2_len = (point_list[0][0] - point_list[2][0]) * (point_list[0][0] - point_list[2][0]) + \
                 (point_list[0][1] - point_list[2][1]) * (point_list[0][1] - point_list[2][1])
        if b1_len == 0:
            return False
        if b1_len != b2_len:
            return False
        b3_len = (point_list[3][0] - point_list[1][0]) * (point_list[3][0] - point_list[1][0]) + \
                 (point_list[3][1] - point_list[1][1]) * (point_list[3][1] - point_list[1][1])
        b4_len = (point_list[3][0] - point_list[2][0]) * (point_list[3][0] - point_list[2][0]) + \
                 (point_list[3][1] - point_list[2][1]) * (point_list[3][1] - point_list[2][1])
        if b1_len != b3_len:
            return False
        if b3_len != b4_len:
            return False
        k1 = (point_list[1][1] - point_list[0][1]) * (point_list[2][1] - point_list[0][1])
        k2 = (point_list[2][0] - point_list[0][0]) * (point_list[0][0] - point_list[1][0])
        if k1 == k2:
            return True
        if k1 == 0 and (k2 == 1 or k2 == -1):
            return True
        if k2 == 0 and (k1 == 1 or k1 == -1):
            return True
        return False
s = Solution()
print('t',s.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
print('f',s.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]))
print('t',s.validSquare(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]))
print('t',s.validSquare([1134,-2539], [492,-1255], [-792,-1897], [-150,-3181]))