import time
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # TODO: 2020.4.5
        pass


if __name__ == "__main__":
    testCases = [([1, 1, 1, 1, 1], 3, 5)]
    for i, testCase in enumerate(testCases):
        nums, S, ans = testCase
        tic = time.time()
        ret = Solution().findTargetSumWays(nums, S)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.5f}s.")
