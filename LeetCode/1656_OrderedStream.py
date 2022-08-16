from typing import List
class OrderedStream:

    def __init__(self, n: int):
        self.dict = {}
        self.ptr = 0
        self.n = n


    def insert(self, idKey: int, value: str) -> List[str]:
        self.dict[idKey] = value
        if idKey - 1 == self.ptr:
            ret = []
            for i in range(idKey, self.n + 1):
                if i in self.dict:
                    self.ptr = (self.ptr + 1) % self.n
                    ret.append(self.dict[i])
                else:
                    return ret
            return ret
        return []








# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)