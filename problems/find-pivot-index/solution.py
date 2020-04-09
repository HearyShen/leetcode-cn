import time
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        accumulate = 0
        for left in range(len(nums)):
            if accumulate == (total - nums[left]) / 2:
                return left
            accumulate += nums[left]
        return -1


if __name__ == '__main__':
    testCases = [([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1), ([-1,-1,-1,-1,-1,-1], -1)]
    for i, testCase in enumerate(testCases):
        nums, ans = testCase
        tic = time.time()
        ret = Solution().pivotIndex(nums)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")