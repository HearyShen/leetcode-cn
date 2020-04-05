import time
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """Solved by DFS with DP cache."""
        if not nums:
            return 0
        numsLen = len(nums)
        dfsCache = {}   # cache for DFS dynamic plan

        def dfs(s, index):
            if index == numsLen:
                return 1 if s == S else 0
            if (s, index) in dfsCache:  # if this sub-problem has been solved
                return dfsCache[(s, index)]
            else:                       # if this sub-problem is first met
                plus = dfs(s + nums[index], index + 1)
                minus = dfs(s - nums[index], index + 1)
                sumWays = plus + minus
                dfsCache[(s, index)] = sumWays
            return sumWays

        return dfs(0, 0)


if __name__ == "__main__":
    testCases = [([1, 1, 1, 1, 1], 3, 5),
                 ([6, 20, 22, 38, 11, 15, 22, 30, 0, 17, 34, 29, 7, 42, 46, 49, 30, 7, 14, 5], 28, 6738)
                 ]
    for i, testCase in enumerate(testCases):
        nums, S, ans = testCase
        tic = time.time()
        ret = Solution().findTargetSumWays(nums, S)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc - tic:.5f}s.")
