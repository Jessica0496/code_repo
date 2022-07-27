import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        fraction_list = []
        cur = ''
        op_list = []
        for i, n in enumerate(expression):
            if n == '-' or n == '+':
                op_list.append(n)
                fraction_list.append(cur)
                cur = ''
            else:
                cur += n
        if cur:
            fraction_list.append(cur)
        def yuefen(numerator, denominator):
            tmp = math.gcd(numerator, denominator)
            return str(numerator//tmp) + '/' + str(denominator//tmp)
        def count_fraction(left, op, right):
            if not left:
                return op+right
            left_numerator, left_denominator = int(left.split('/')[0]), int(left.split('/')[1])
            right_numerator, right_denominator = int(right.split('/')[0]), int(right.split('/')[1])
            if left_denominator == right_denominator:
                if op == '+':
                    left_numerator += right_numerator
                else:
                    left_numerator -= right_numerator
                return yuefen(left_numerator, left_denominator)
            else:
                left_numerator *= right_denominator
                if op == '+':
                    left_numerator += (right_numerator * left_denominator)
                else:
                    left_numerator -= right_numerator * left_denominator
                return yuefen(left_numerator, left_denominator*right_denominator)
        left = fraction_list[0]
        for op, right in zip(op_list, fraction_list[1:]):
            left = count_fraction(left, op, right)
        return left
s = Solution()
print('0/1',s.fractionAddition(expression = "-1/2+1/2"))
print('1/3',s.fractionAddition(expression = "-1/2+1/2+1/3"))
print('-1/6',s.fractionAddition(expression = "1/3-1/2"))
