import time


class Solution:
    def decodeString(self, s: str) -> str:
        """
        Use auxiliary stack to save curMul and lastRes.
        Referenced from solution: https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
        """
        if not s:
            return ''

        stack = []
        mul = 0
        res = ''
        for i, c in enumerate(s):
            if c.isdigit():
                mul = mul * 10 + int(c)
            elif c == '[':
                stack.append((mul, res))
                res = ''
                mul = 0
            elif c.isalpha():
                res += c
            elif c == ']':
                curMul, lastRes = stack.pop()
                res = lastRes + curMul * res

        return res


if __name__ == '__main__':
    testCases = [("3[a]2[bc]", "aaabcbc"), ("3[a2[c]]", "accaccacc"), ("2[abc]3[cd]ef", "abcabccdcdcdef")]
    for i, testCase in enumerate(testCases):
        s, ans = testCase
        tic = time.time()
        ret = Solution().decodeString(s)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")