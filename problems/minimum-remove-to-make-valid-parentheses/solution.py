import time


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # TODO: 2020.3.9


if __name__ == "__main__":
    testCases = [("lee(t(c)o)de)", "lee(t(c)o)de"), ("a)b(c)d", "ab(c)d"), ("))((", ""), ("(a(b(c)d)", "a(b(c)d)")]

    for i, testCase in enumerate(testCases):
        s, ans = testCase
        tic = time.time()
        ret = Solution().minRemoveToMakeValid(s)
        toc = time.time()
        print(f"{i}: {ret == ans}, {ret} in {toc-tic:.3f}s.")