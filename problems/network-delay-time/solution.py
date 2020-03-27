import time
from typing import List
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # dijkstra shortest-path algorithm
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # initialize distance
        dist = {node: float('inf') for node in range(1, N+1)}   # distances are default as inf
        dist[K] = 0     # single source from node K
        seen = [False] * (N+1)
        
        while True:
            # find min-dist node from source
            minDistNode = -1
            cand_dist = float('inf')
            for i in range(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    minDistNode = i
            # if all node have been seen
            if minDistNode < 0: 
                break
            else:
                seen[minDistNode] = True
                for neighbor, dist2neighbor in graph[minDistNode]:    # find min distance to candidate's neighbors
                    dist[neighbor] = min(dist[neighbor], dist[minDistNode] + dist2neighbor)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1


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