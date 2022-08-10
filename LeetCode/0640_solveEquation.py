class Solution:
    def solveEquation(self, equation: str) -> str:
        stack = []
        ops = []
        flag = False
        if equation[0] != '-':
            start = 0
        else:
            start = 1
            flag = True
        for i in range(1, len(equation)):
            if equation[i] in '+-=':
                cur = equation[start: i]
                stack.append(cur)
                start = i+1
                ops.append(equation[i])
        stack.append(equation[start:])
        def count(n, op, k, b):
            if not n:
                return k, b
            if op == '-':
                if n.isdigit():
                    b -= int(n)
                elif n == 'x':
                    k -= 1
                else:
                    k -= int(n.rstrip('x'))
            else:
                if n.isdigit():
                    b += int(n)
                elif n == 'x':
                    k += 1
                else:
                    k += int(n.rstrip('x'))
            return k, b
        cur = stack.pop(0)
        k = 0
        b = 0

        if cur.isdigit():
            b = int(cur)
            if flag:
                b = -1 * b
        elif cur == 'x':
            k = 1
            if flag:
                k = -1
        else:
            k = int(cur.rstrip('x'))
            if flag:
                k = -1 * k
        for n, op in zip(stack, ops):
            if op == '=':
                k, b = count(n, '+', -1*k, -1*b)
            else:
                k, b = count(n, op, k, b)
        if k == 0:
            if b != 0:
                return "No solution"
            else:
                return "Infinite solutions"
        return 'x='+str(-1 * (b//k))

s = Solution()
print('x=2', s.solveEquation("x+5-3+x=6+x-2"))
print("Infinite solutions", s.solveEquation("x=x"))
print('x=0', s.solveEquation("2x=x"))
print('No solution',s.solveEquation("x=x+2"))
print("x=1", s.solveEquation("-x=-1"))
print("x=-1", s.solveEquation("-x=1"))