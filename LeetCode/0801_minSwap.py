from typing import List
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = 1
        for i in range(1, n):
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                    # 同时满足1，2两个条件
                    dp[i][0] = min(dp[i-1][0], dp[i-1][1])
                    dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
                else:
                    # 只满足1
                    dp[i][0] = dp[i-1][0]
                    dp[i][1] = dp[i-1][1] + 1
            elif nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                # 只满足2
                dp[i][0] = dp[i - 1][1]
                dp[i][1] = dp[i - 1][0] + 1
        return min(dp[-1])




s = Solution()
print('1', s.minSwap(nums1 = [1,3,5,4], nums2 = [1,2,3,7]))
print('1', s.minSwap(nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]))