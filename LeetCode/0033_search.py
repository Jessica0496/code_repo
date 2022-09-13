'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O ( l o g n ) O(log n)O(logn) 级别。
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            '''
            常规解法，先二分找到转折点，再二分查找
             三种情况向前规约，其他情况都是向后规约
             nums[0] <= target <= nums[i] 0~i是正序，target小于mid【0，mid】
             target <= nums[i] < nums[0] 0~i是转折过的，而target小于mid，【转折，mid】
             nums[i] < nums[0] <= target 0~i是转折过的，而target大于0，【0，转折】
             因此需要判断
             (nums[0] <= target)， (target <= nums[i]) ，(nums[i] < nums[0])
             异或操作：两项为真异或为假，只有一项为真异或是真
             两项为真时向前规约
            '''
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                left = mid + 1
            else:
                right = mid
        return left if left == right and nums[left] == target else -1
s = Solution()
print(s.search([4,5,6,7,0,1,2], 5))
print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([4,5,6,7,0,1,2], 7))
print(s.search([4,5,6,7,0,1,2], 0))
