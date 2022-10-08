from typing import List
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        idx1, idx2 = list(range(n)), list(range(n))
        idx1.sort(key=lambda x: nums1[x])
        idx2.sort(key=lambda x: nums2[x])
        ret = [0] * n
        left, right = 0, n-1
        for i in range(n):
            if nums1[idx1[i]] > nums2[idx2[left]]:
                ret[idx2[left]] = nums1[idx1[i]]
                left += 1
            else:
                ret[idx2[right]] = nums1[idx1[i]]
                right -= 1
        return ret
s = Solution()
print('[2,11,7,15]', s.advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11]))
print('[24,32,8,12]', s.advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11]))