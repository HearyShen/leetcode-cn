import time
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if not stack:
                stack.append(token)
            if token in {'+', '-', '*', '/'}:
                y = stack.pop()
                x = stack.pop()

                if token == '+':
                    stack.append(x+y)
                elif token == '-':
                    stack.append(x-y)
                elif token == '*':
                    stack.append(x*y)
                elif token == '/':
                    stack.append(int(x/y))
            else:
                stack.append(int(token))
        return stack.pop()


if __name__ == "__main__":
    testCases = [
        (["2", "1", "+", "3", "*"], 9), 
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)
    ]
    for i, testCase in enumerate(testCases):
        tokens, ans = testCase
        tic = time.time()
        ret = Solution().evalRPN(tokens)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
