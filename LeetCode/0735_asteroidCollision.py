from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        def compare(i):
            if not stack or i > 0:
                stack.append(i)
            elif stack[-1] < 0 and i < 0:
                stack.append(i)
            else:
                tmp = stack.pop()
                if i < 0 and i + tmp < 0:
                    compare(i)
                elif i < 0 and i + tmp > 0:
                    stack.append(tmp)
        for i in asteroids:
            compare(i)
        return stack




s = Solution()
print('[5,10]', s.asteroidCollision([5,10,-5]))
print('[]', s.asteroidCollision([8,-8]))
print('[10]', s.asteroidCollision([10,2,-5]))
print('[-2,-1,1,2]', s.asteroidCollision([-2,-1,1,2]))  # 不会相交