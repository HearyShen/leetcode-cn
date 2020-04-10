import time


class Solution:
    def solveEquation(self, equation: str) -> str:
        # TODO: 2020.4.11
        pass


if __name__ == '__main__':
    testCases = [("x+5-3+x=6+x-2", "x=2"), ("x=x", "Infinite solutions"), ("2x=x", "x=0"), ("2x+3x-6x=x+2", "x=-1"),
                 ("x=x+2", "No solution")]
    for i, testCase in enumerate(testCases):
        equation, ans = testCase
        tic = time.time()
        ret = Solution.solveEquation(equation)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
