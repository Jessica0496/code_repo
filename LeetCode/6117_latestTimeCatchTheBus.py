from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        i, j = 0, 0
        cur = capacity
        while i < len(buses) and j < len(passengers):
            if i == len(buses) - 1 and j == len(passengers) - 1:
                if cur == 1:
                    tmp = min(passengers[j], buses[i])
                    for k in range(tmp):
                        if tmp - k not in passengers:
                            return tmp - k
                elif buses[i] > passengers[j]:
                    return buses[i]
                else:
                    tmp = min(passengers[j], buses[i])
                    for k in range(tmp):
                        if tmp - k not in passengers:
                            return tmp - k
            elif i == len(buses) - 1 and cur == 1:
                tmp = min(passengers[j], buses[i])
                for k in range(tmp):
                    if tmp - k not in passengers:
                        return tmp - k
            elif i == len(buses) - 1 and passengers[j] > buses[i]:
                return buses[i]
            elif i == len(buses) - 1 and passengers[j] == buses[i]:
                tmp = buses[i]
                for k in range(tmp):
                    if tmp - k not in passengers:
                        return tmp - k
            elif passengers[j] <= buses[i] and cur > 0:
                cur -= 1
                j += 1
            elif passengers[j] <= buses[i] and cur == 0:
                i += 1
                cur = capacity
            elif passengers[j] > buses[i]:
                i += 1
                cur = capacity
        if i < len(buses):
            return buses[-1]


s = Solution()
print('16',s.latestTimeCatchTheBus(buses = [10,20], passengers = [2,17,18,19], capacity = 2))
print('20', s.latestTimeCatchTheBus(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2))
print('1',s.latestTimeCatchTheBus([2], [2], 2))
print('3',s.latestTimeCatchTheBus([3], [2], 2))
print('5',s.latestTimeCatchTheBus([5], [7,8], 1))
print('11',s.latestTimeCatchTheBus([18,8,3,12,9,2,7,13,20,5],[13,10,8,4,12,14,18,19,5,2,30,34],1))
print('1',s.latestTimeCatchTheBus([3],[2],1))
print('18',s.latestTimeCatchTheBus([6,8,18,17],[6,8,17],1))
print('19',s.latestTimeCatchTheBus([14,10,4,5,7,2,11,19,16,9],[3,39,45,30,40,50,13,15,34,5],3))