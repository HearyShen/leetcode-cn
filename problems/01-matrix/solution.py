import time
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # TODO: 2020.4.8
        pass

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
    )
    ]
    for i, testCase in enumerate(testCases):
        matrix, ans = testCase
        tic = time.time()
        ret == Solution().updateMatrix(matrix)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
