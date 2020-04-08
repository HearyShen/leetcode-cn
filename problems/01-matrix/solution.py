import time
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """Solve with DP"""
        # TODO: 2020.4.8
        rLen, cLen = len(matrix), len(matrix[0])
        
        for r in range(rLen):
            for c in range(cLen):
                if matrix[r][c] == 1:
                    up = matrix[r-1][c] if r-1 >=0 else 1
                    down = matrix[r+1][c] if r+1 < rLen else 1
                    left = matrix[r][c-1] if c-1 >= 0 else 1
                    right = matrix[r][c+1] if c+1 < cLen else 1
                    matrix[r][c] = min(up, down, left, right) + 1
        return matrix


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
