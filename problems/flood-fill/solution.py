import time
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """Solve with BFS"""
        if not image or image[sr][sc] == newColor:
            return image
        rLen, cLen = len(image), len(image[0])
        oldColor = image[sr][sc]
        deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        bfsQueue = [(sr, sc)]
        while bfsQueue:
            # render the current one
            curR, curC = bfsQueue.pop(0)
            image[curR][curC] = newColor
            # append the valid neighbors to bfsQueue
            nextRCs = [
                (curR + delta[0], curC + delta[1]) for delta in deltas
                if 0 <= (curR + delta[0]) < rLen 
                and 0 <= (curC + delta[1]) < cLen 
                and image[curR + delta[0]][curC + delta[1]] == oldColor
            ]
            bfsQueue.extend(nextRCs)
        return image


if __name__ == "__main__":
    testCases = [([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
    ([[0,0,0],[0,1,1]], 1, 1, 1, [[0,0,0],[0,1,1]])]
    for i, testCase in enumerate(testCases):
        image, sr, sc, newColor, ans = testCase
        tic = time.time()
        ret = Solution().floodFill(image, sr, sc, newColor)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")