import time
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # TODO: 2020.4.10, too slow, out of time
        minSumLeft = 0
        minSumRight = len(nums)
        hasFound = False
        for left in range(len(nums)):
            curSum = 0
            for right in range(left, len(nums)):
                curSum += nums[right]
                if s <= curSum and right - left < minSumRight - minSumLeft:
                    hasFound = True
                    minSumLeft = left
                    minSumRight = right
        print(f"({minSumLeft}, {minSumRight})")
        return minSumRight + 1 - minSumLeft if hasFound else 0


if __name__ == '__main__':
    testCases = [(7, [2, 3, 1, 2, 4, 3], 2), (15, [1, 2, 3, 4, 5], 5)]
    for i, testCase in enumerate(testCases):
        s, nums, ans = testCase
        tic = time.time()
        ret = Solution().minSubArrayLen(s, nums)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc - tic:.3f}s.")
