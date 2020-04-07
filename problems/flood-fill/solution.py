import time
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # TODO: 2020.4.7
        pass


if __name__ == "__main__":
    testCases = [([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2, [[2,2,2],[2,2,0],[2,0,1]])]
    for i, testCase in enumerate(testCases):
        image, sr, sc, newColor, ans = testCase
        tic = time.time()
        ret = Solution().floodFill(image, sr, sc, newColor)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")