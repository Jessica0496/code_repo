import copy


class MyCircularQueue:

    def __init__(self, k: int):
        self.dict = {}
        self.length = k
    def enQueue(self, value: int) -> bool:
        cur_pos = len(self.dict)
        if cur_pos < self.length:
            self.dict[cur_pos + 1] = value
            return True
        return False
    def deQueue(self) -> bool:
        cur_pos = len(self.dict)
        if cur_pos > 0:
            self.dict.pop(1)
            self.tmp_q = {}
            for k, v in self.dict.items():
                self.tmp_q[k - 1] = v
            self.dict = copy.deepcopy(self.tmp_q)
            return True
        return False
    def Front(self) -> int:
        cur_pos = len(self.dict)
        if cur_pos > 0:
            return self.dict[1]
        return -1
    def Rear(self) -> int:
        cur_pos = len(self.dict)
        if cur_pos > 0:
            return self.dict[cur_pos]
        return -1
    def isEmpty(self) -> bool:
        return len(self.dict) == 0


    def isFull(self) -> bool:
        return len(self.dict) == self.length



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()