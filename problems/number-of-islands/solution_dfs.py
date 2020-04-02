import time
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        self.grid = grid
        self.islandsCount = 0
        self.deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        self.yLen, self.xLen = len(grid), len(grid[0])
        for yIdx in range(self.yLen):
            for xIdx in range(self.xLen):
                if self.grid[yIdx][xIdx] == "1":
                    hasIsland = self.dfs(yIdx, xIdx)
                    if hasIsland:
                        self.islandsCount += 1
        return self.islandsCount

    def dfs(self, y, x):
        if self.grid[y][x] == '0':
            return False
        
        self.grid[y][x] = '0'
        for delta in self.deltas:
            nextY, nextX = y + delta[0], x + delta[1]
            if 0<=nextY<self.yLen and 0<=nextX<self.xLen and self.grid[nextY][nextX] == '1':
                self.dfs(nextY, nextX)
        return True


if __name__ == "__main__":
    testCases = [([
        ["1", "1", "1", "1", "0"], 
        ["1", "1", "0", "1", "0"], 
        ["1", "1", "0", "0", "0"], 
        ["0", "0", "0", "0", "0"]], 1)]

    for i, testCase in enumerate(testCases):
        grid, ans = testCase
        tic = time.time()
        ret = Solution().numIslands(grid)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
