class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ori = '123456789'
        newI = ori[:len(pattern) + 1]
        maxReverse = 1
        tmpI = 0
        for i in range(len(pattern)):
            if pattern[i] == 'D':
                if maxReverse == 1:
                    tmpI = i
                maxReverse += 1
            else:
                if maxReverse == 1:
                    continue
                if tmpI > 0:
                    newI = newI[:tmpI] + newI[i:tmpI - 1:-1] + newI[i + 1:]
                else:
                    newI = newI[:i+1][::-1] + newI[i + 1:]

                maxReverse = 1
        if maxReverse > 1:
            if tmpI == 0:
                return newI[::-1]
            newI = newI[:tmpI] + newI[len(pattern) + 1:tmpI - 1:-1]
        return newI
s = Solution()
print("4321567", s.smallestNumber("DDDIII"))
print("123549876", s.smallestNumber("IIIDIDDD"))
print("4321", s.smallestNumber("DDD"))