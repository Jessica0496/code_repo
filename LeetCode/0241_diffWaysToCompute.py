from typing import List
ADDITION = -1
SUBTRACTION = -2
MULTIPLICATION = -3

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = []
        i, n = 0, len(expression)
        while i < n:
            if expression[i].isdigit():
                x = 0
                while i < n and expression[i].isdigit():
                    x = x * 10 + int(expression[i])
                    i += 1
                ops.append(x)
            else:
                if expression[i] == '+':
                    ops.append(ADDITION)
                elif expression[i] == '-':
                    ops.append(SUBTRACTION)
                else:
                    ops.append(MULTIPLICATION)
                i += 1

        n = len(ops)
        dp = [[[] for _ in range(n)] for _ in range(n)]
        for i, x in enumerate(ops):
            dp[i][i] = [x]
        for sz in range(3, n + 1):
            for r in range(sz - 1, n, 2):
                l = r - sz + 1
                for k in range(l + 1, r, 2):
                    for x in dp[l][k - 1]:
                        for y in dp[k + 1][r]:
                            if ops[k] == ADDITION:
                                dp[l][r].append(x + y)
                            elif ops[k] == SUBTRACTION:
                                dp[l][r].append(x - y)
                            else:
                                dp[l][r].append(x * y)
        return dp[0][-1]

s = Solution()
print('[0,2]', s.diffWaysToCompute(expression="2-1-1"))
print('[-34,-14,-10,-10,10]', s.diffWaysToCompute(expression="2*3-4*5"))