import time
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        outs = []
        deltas = [[0,1], [1,0], [0,-1], [-1,0]]     # right, down, left, up
        mode = 0
        upBound, downBound, leftBound, rightBound = 0, len(matrix), 0, len(matrix[0])
        r, c = 0, 0
        while upBound <= r < downBound and leftBound <= c < rightBound:
            outs.append(matrix[r][c])
            if not (upBound <= r+deltas[mode][0] < downBound and leftBound <= c+deltas[mode][1] < rightBound):
                if mode == 0:
                    upBound += 1
                elif mode == 1:
                    rightBound -= 1
                elif mode == 2:
                    downBound -= 1
                else:
                    leftBound += 1
                mode = (mode + 1) % 4   # change mode
            # move to next according current mode
            r += deltas[mode][0]
            c += deltas[mode][1]
        return outs


if __name__ == "__main__":
    testCases = [([
                      [1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]
                  ], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
                ([
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]
                ], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    ]
    for i, testCase in enumerate(testCases):
        matrix, ans = testCase
        tic = time.time()
        ret = Solution().spiralOrder(matrix)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc - tic:.3f}s.")
