from typing import List
from collections import defaultdict
from itertools import combinations, permutations
import copy
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        num_set = set(i for i in range(1, k + 1))
        tmp_for_remove = copy.deepcopy(num_set)
        ans = 1
        for n in rolls:
            if n in tmp_for_remove:
                tmp_for_remove.remove(n)
                if not tmp_for_remove:
                    tmp_for_remove = copy.deepcopy(num_set)
                    ans += 1
        return ans
   


s = Solution()
print(s.shortestSequence(rolls = [4,2,1,2,3,3,2,4,1], k = 4))
print('6',s.shortestSequence([3,2,1,3,3,3,3,3,1,2,2,3,1,3,3,1,1,3,1,1,1,3,1,3,3,1,2,3,2,1,1,2],3))




