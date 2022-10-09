class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i, b in enumerate(s):
            if b == '(':
                stack.append('(')
            elif b == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    cur = stack.pop()
                    while stack and stack[-1] != '(':
                        cur += stack.pop()
                    if stack[-1] == '(':
                        stack.pop()
                        cur *= 2
                        stack.append(cur)
        return sum(stack)
s = Solution()
print('2', s.scoreOfParentheses("(())"))
print('2', s.scoreOfParentheses("()()"))
print('6', s.scoreOfParentheses("(()(()))"))
