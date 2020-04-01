import time
import math


class Solution:
    def numSquares(self, n: int) -> int:
        if n < 0:
            return -1

        maxBase = int(math.sqrt(n))
        squares = [base**2 for base in range(1, maxBase+1)]     # from large to small
        visited = {n}
        step = 0
        bfsQueue = [n]
        while bfsQueue:
            for _ in range(len(bfsQueue)):
                curNode = bfsQueue.pop(0)
                if curNode == 0:
                    return step
                # search branches
                nextNodes = [curNode - square for square in squares[::-1] if square <= curNode and (curNode - square) not in visited]
                visited.update(nextNodes)
                bfsQueue.extend(nextNodes)
                # print(f"{curNode} -> {nextNodes}")
            step += 1
        return -1


if __name__ == "__main__":
    testCases = [(12, 3), (13, 2)]
    for i, testCase in enumerate(testCases):
        n, ans = testCase
        tic = time.time()
        ret = Solution().numSquares(n)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")