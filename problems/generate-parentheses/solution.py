import time
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # TODO: 2020.4.9
        pass


if __name__ == "__main__":
    testCases = [(3, [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()"
    ])]

    for i, testCase in enumerate(testCases):
        n, ans = testCase
        tic = time.time()
        ret = Solution().generateParenthesis(n)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
