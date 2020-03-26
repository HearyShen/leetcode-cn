import time
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if not times or N < 1 or K < 1:
            return -1

        delays = [[-1 for i in range(N)] for i in range(N)]  # default as -1

        # set default weight matrix
        for timeIn in times:
            u, v, w = timeIn
            delays[u - 1][v - 1] = w

        # maxDelay = 0
        nodeDelays = [-1 for i in range(N)]
        visited = set()
        bfsQueue = [(K - 1, 0)]
        while bfsQueue:
            curNode, curDelay = bfsQueue.pop(0)
            visited.add(curNode)
            if nodeDelays[curNode] < 0 or nodeDelays[curNode] > curDelay:
                nodeDelays[curNode] = curDelay
            print(f"{curNode+1}: {curDelay}")
            # find next
            for nextNode, nextDelay in enumerate(delays[curNode]):
                if nextDelay >= 0 and nextNode not in visited:  # valid node
                    bfsQueue.append((nextNode, curDelay + nextDelay))
                    print(f"{curNode+1}->{nextNode+1}: {curDelay+nextDelay}")

        if len(visited) == N:
            return max(nodeDelays)
        return -1


if __name__ == "__main__":
    testCases = [([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
                 ([[1, 2, 1], [2, 3, 2], [1, 3, 2]], 3, 1, 2),
                 ([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1, 3),
                 ([[2, 4, 10], [5, 2, 38], [3, 4, 33], [4, 2, 76], [3, 2, 64],
                   [1, 5, 54], [1, 4, 98], [2, 3, 61], [2, 1, 0], [3, 5, 77],
                   [5, 1, 34], [3, 1, 79], [5, 3, 2], [1, 2, 59], [4, 3, 46],
                   [5, 4, 44], [2, 5, 89], [4, 5, 21], [1, 3, 86],
                   [4, 1, 95]], 5, 1, 69)]
    for i, testCase in enumerate(testCases):
        times, N, K, ans = testCase
        tic = time.time()
        ret = Solution().networkDelayTime(times, N, K)
        toc = time.time()
        print(f"{i}: {ret==ans}, return {ret} in {toc-tic:.3f}s.")