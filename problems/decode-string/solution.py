import time


class Solution:
    def decodeString(self, s: str) -> str:
        # TODO: 2020.4.7
        pass


if __name__ == '__main__':
    testCases = [("3[a]2[bc]", "aaabcbc"), ("3[a2[c]]", "accaccacc"), ("2[abc]3[cd]ef", "abcabccdcdcdef")]
    for i, testCase in enumerate(testCases):
        s, ans = testCase
        tic = time.time()
        ret = Solution().decodeString(s)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")