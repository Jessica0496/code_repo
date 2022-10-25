from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(grid[i]):
                if v != 1:
                    continue
                island = []
                grid[i][j] = -1
                q = [(i, j)]
                while q:
                    x, y = q.pop(0)
                    island.append((x,y))
                    for l, r in [(-1,0),(0, 1),(1, 0), (0,-1)]:
                        if 0 <= x+l < n and 0 <= y + r < n:
                            if grid[x+l][y+r] == 1:
                                grid[x + l][y + r] = -1
                                q.append((x+l, y+r))
                step = 0
                q = island
                while True:
                    tmp = q
                    q = []
                    for x, y in tmp:
                        for l, r in [(-1,0),(0, 1),(1, 0), (0,-1)]:
                            if 0 <= x+l < n and 0 <= y + r < n:
                                if grid[x+l][y+r] == 1:
                                    return step
                                if grid[x + l][y + r] == 0:
                                    grid[x + l][y + r] = -1
                                    q.append((x+l, y+r))
                    step += 1
s = Solution()
print('1', s.shortestBridge(grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
print('1', s.shortestBridge(grid = [[0,1],[1,0]]))
print('2', s.shortestBridge(grid = [[0,1,0],[0,0,0],[0,0,1]]))