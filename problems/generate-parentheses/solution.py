import time
from typing import List
from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """Solved with BFS"""
        bfsQueue = deque()
        bfsQueue.append([1])  # start from '('
        num2par = {1: '(', -1: ')'}     # represent '('/')' as 1/-1 for quick valid check
        valid = []
        depth = 0
        while bfsQueue and depth < n*2:
            depth += 1
            for _ in range(len(bfsQueue)):
                curPath = bfsQueue.popleft()
                curPathSum = sum(curPath)
                # check valid
                if len(curPath) == n*2 and curPathSum == 0:
                    valid.append(''.join([num2par[num] for num in curPath]))
                # append next
                if len(curPath) >= n*2:     # BFS search don't have to exceed 2n
                    continue
                if curPathSum + 1 <= n:     # add a '(' if '('s are not too many
                    bfsQueue.append(curPath + [1])
                if 0 <= curPathSum - 1:     # add a ')' if ')'s are not too many
                    bfsQueue.append(curPath + [-1])
        return valid


if __name__ == "__main__":
    testCases = [
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        (4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])]

    for i, testCase in enumerate(testCases):
        n, ans = testCase
        tic = time.time()
        ret = Solution().generateParenthesis(n)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
