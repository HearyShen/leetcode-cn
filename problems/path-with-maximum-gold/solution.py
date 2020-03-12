import time
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # goldPlans = set()
        # for y in range(len(grid)):
        #     for x in range(len(grid[0])):
        #         goldPlans.add(self.dfsDigGold(grid, (y, x)))
        goldPlans = [self.dfsDigGold(grid, (y,x)) for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] != 0]
        return max(goldPlans)

    def dfsDigGold(self, grid: List[List[int]], loc) -> int:
        y_len, x_len = len(grid), len(grid[0])
        y, x = loc
        curGold = grid[y][x]
        if curGold == 0:
            return 0
        else:
            grid[y][x] = 0
            goldPlans = [0]  # default as 0 (may have no where to dig)
            if y - 1 >= 0:  # dig north
                goldPlans.append(
                    self.dfsDigGold(grid, (y - 1, x)) + curGold)
            if y + 1 < y_len:  # dig south
                goldPlans.append(
                    self.dfsDigGold(grid, (y + 1, x)) + curGold)
            if x - 1 >= 0:  # dig west
                goldPlans.append(
                    self.dfsDigGold(grid, (y, x - 1)) + curGold)
            if x + 1 < x_len:  # dig east
                goldPlans.append(
                    self.dfsDigGold(grid, (y, x + 1)) + curGold)
            grid[y][x] = curGold
            return max(goldPlans)


if __name__ == "__main__":
    testCases = [([[0, 6, 0], [5, 8, 7], [0, 9, 0]], 24),
                 ([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]], 28),
                 ([[5, 3, 36, 26, 27], [11, 31, 23, 30, 4], [5, 7, 21, 38, 10], [39, 30, 10, 17, 13], [16, 0, 0, 26, 1], [25, 0, 10, 0, 0]], 454)]
    for i, testCase in enumerate(testCases):
        grid, ans = testCase
        tic = time.time()
        ret = Solution().getMaximumGold(grid)
        toc = time.time()
        print(f"{i}: {ret == ans}, {ret} in {toc-tic:.3f}s.")