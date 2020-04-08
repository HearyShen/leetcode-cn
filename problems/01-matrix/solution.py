import time
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """Solve with DP"""
        # TODO: 2020.4.8
        rLen, cLen = len(matrix), len(matrix[0])
        # dist = [[10000] * cLen] * rLen    # ALERT: all the rows actually point to only one list
        dist = [[1000000 for i in range(cLen)] for j in range(rLen)]
        for r in range(rLen):
            for c in range(cLen):
                if matrix[r][c] == 0:
                    dist[r][c] = 0
                else:
                    if r - 1>= 0:
                        dist[r][c] = min(dist[r][c], dist[r-1][c] + 1)
                    if c - 1 >= 0:
                        dist[r][c] = min(dist[r][c], dist[r][c-1] + 1)

        for r in range(rLen-1, -1, -1):     # dist_[rLen-1, -1) == dist_(rLen, 0]
            for c in range(cLen-1, -1, -1):
                if r + 1 < rLen:
                    dist[r][c] = min(dist[r][c], dist[r+1][c] + 1)
                if c + 1 < cLen:
                    dist[r][c] = min(dist[r][c], dist[r][c+1] + 1)

        return dist


if __name__ == "__main__":
    testCases = [(
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    ),
    (
        [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]
        ],
        [
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 1]
        ]
    ), 
    (
        [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]],
        [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
    )
    ]
    for i, testCase in enumerate(testCases):
        matrix, ans = testCase
        tic = time.time()
        ret = Solution().updateMatrix(matrix)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
