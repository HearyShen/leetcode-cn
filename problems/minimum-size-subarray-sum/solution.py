import time
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # TODO: 2020.4.10
        pass


if __name__ == '__main__':
    testCases = [(7, [2, 3, 1, 2, 4, 3], 2)]
    for i, testCase in enumerate(testCases):
        s, nums, ans = testCase
        tic = time.time()
        ret = Solution.minSubArrayLen(s, nums)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc - tic:.3f}s.")
