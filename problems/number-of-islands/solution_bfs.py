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
                    hasIsland = self.bfs(yIdx, xIdx)
                    if hasIsland:
                        self.islandsCount += 1
        return self.islandsCount
                
    def bfs(self, y, x):
        if self.grid[y][x] == "0":
            return False
        
        bfsQueue = [(y,x)]
        self.grid[y][x] = "0"
        while bfsQueue:
            curY, curX = bfsQueue.pop(0)
            
            for delta in self.deltas:
                nextY = curY + delta[0]
                nextX = curX + delta[1]
                if 0<=nextY<self.yLen and 0<=nextX<self.xLen and self.grid[nextY][nextX] == '1':
                    bfsQueue.append((nextY, nextX))
                    self.grid[nextY][nextX] = "0"   # NOTE: important, mark it once reach it to avoid repeating search
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