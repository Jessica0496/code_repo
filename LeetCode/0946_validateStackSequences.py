from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while popped:
            cur = popped.pop(0)
            if stack and stack[-1] == cur:
                stack.pop()
            else:
                if not pushed:
                    return False
                node = pushed.pop(0)
                while node != cur:
                    stack.append(node)
                    if not pushed:
                        return False
                    node = pushed.pop(0)
        return True
s = Solution()
print('t', s.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))
print('f', s.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))
print('f', s.validateStackSequences([1,2,3,4,5,6,7], [1,2,5,3,6,7,4]))
