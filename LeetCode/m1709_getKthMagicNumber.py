class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0] * (k + 1)
        dp[1] = 1
        p3 = p5 = p7 = 1
        for i in range(2, k + 1):
            n3, n5, n7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
            dp[i] = min(n3, n5, n7)
            if dp[i] == n3:
                p3 += 1
            if dp[i] == n5:
                p5 += 1
            if dp[i] == n7:
                p7 += 1
        return dp[k]


s = Solution()
print('9', s.getKthMagicNumber(5))
print('3215625', s.getKthMagicNumber(251))
