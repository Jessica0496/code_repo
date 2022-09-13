class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        n = len(num_list)
        idx1 = idx2 = -1
        max_idx = n - 1
        for i in range(n - 1, -1, -1):
            if num_list[i] > num_list[max_idx]:
                max_idx = i
            elif num_list[i] < num_list[max_idx]:
                idx1, idx2 = i, max_idx
        if idx1 < 0:
            return num
        num_list[idx1], num_list[idx2] = num_list[idx2], num_list[idx1]
        return int(''.join(num_list))
s = Solution()
print('98863', s.maximumSwap(98368))