import copy
from typing import List
from collections import defaultdict
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        wei2num = {}
        length = len(nums[0])
        for i in range(1, length):
            tmp = []
            for j in nums:
                tmp.append(int(j[-i:]))
            wei2num[i] = tmp
        # print(wei2num)
        ret = []
        for max_num, le in queries:
            if le >= length:
                tmp = nums
            else:
                tmp = wei2num[le]
            num_idx = []
            for i, n in enumerate(tmp):
                num_idx.append([n, i])
            a = copy.deepcopy(num_idx)
            a.sort()
            ret.append(a[max_num-1][1])
        return ret



s = Solution()
print('[2,2,1,0]', s.smallestTrimmedNumbers(nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]))
print('[3,0]', s.smallestTrimmedNumbers(nums = ["24","37","96","04"], queries = [[2,1],[2,2]]))

