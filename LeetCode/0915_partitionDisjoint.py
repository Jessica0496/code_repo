from typing import List
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left_max, cur_max, left_pos = nums[0],nums[0], 0
        for i in range(1, n-1):
            cur_max = max(cur_max, nums[i])
            if nums[i] < left_max:
                left_max = cur_max
                left_pos = i
        return left_pos + 1


s = Solution()
print('3',s.partitionDisjoint(nums = [5,0,3,8,6]))
print('4',s.partitionDisjoint(nums = [1,1,1,0,6,12]))
print('1', s.partitionDisjoint([1,1]))