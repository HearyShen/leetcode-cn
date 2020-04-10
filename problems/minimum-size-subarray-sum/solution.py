import time
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """Sovled by moving screen methods."""
        if not nums:
            return 0

        left = 0
        right = 0
        hasFound = False
        screenSum = nums[0]
        minSubLeft, minSubRight = 0, len(nums)
        while 0 <= left <= right < len(nums):
            if screenSum >= s:
                hasFound = True
                if right - left < minSubRight - minSubLeft:
                    minSubLeft = left
                    minSubRight = right
                # try the smaller sub array if screenSum >= s
                screenSum -= nums[left]
                left += 1
            else:
                # enlarge the screen if screenSum < s
                right += 1
                if right < len(nums):
                    screenSum += nums[right]

        return minSubRight + 1 - minSubLeft if hasFound else 0


if __name__ == '__main__':
    testCases = [(7, [2, 3, 1, 2, 4, 3], 2), (15, [1, 2, 3, 4, 5], 5)]
    for i, testCase in enumerate(testCases):
        s, nums, ans = testCase
        tic = time.time()
        ret = Solution().minSubArrayLen(s, nums)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc - tic:.3f}s.")
