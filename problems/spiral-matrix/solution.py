import time
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # TODO: 2020.4.9
        pass


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
