import time


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # TODO: 2020.4.6
        pass


if __name__ == "__main__":
    testCases = [("horse", "ros", 3), ("intention", "execution", 5)]
    for i, testCase in enumerate(testCases):
        word1, word2, ans = testCase
        tic = time.time()
        ret = Solution().minDistance(word1, word2)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")