import time
from typing import List
from collections import defaultdict, Counter

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Detect cycle to find redundant directed connection,
        category as in-degree=2 or out-degree=2 to solve (only-one redundant connection).
        """
        # TODO: 2020.3.30
        if not edges:
            return []
        
        inDegree = Counter()
        outDegree = Counter()
        self.parent = defaultdict(list)
        self.child = defaultdict(list)
        for edge in edges:
            src, dest = edge
            inDegree[dest] += 1
            outDegree[src] += 1
            self.parent[dest].append(src)
            self.child[src].append(dest)

        # If redundant connection exists, then there must be a cycle.

        # 1. in-degree = 2
        # redundant edge is the edge from the parent node in cycle
        maxInDegreeResult = inDegree.most_common(n=1)
        maxInDegreeNode, maxInDegree = maxInDegreeResult[0]
        if maxInDegree == 2:
            maxInDegreeParents = self.parent[maxInDegreeNode]
            for parentNode in maxInDegreeParents:
                if self.isInCycle_ParentDirection(parentNode):
                    return [parentNode, maxInDegreeNode]

        # 2. out-degree = 2
        # redundant edge is any edge in the cycle
        maxOutDegreeResult = outDegree.most_common(n=1)
        maxOutDegreeNode, maxOutDegree = maxOutDegreeResult[0]
        if maxOutDegree == 2:
            maxOutDegreeChildren = [edge[1] for edge in edges if edge[0]==maxOutDegreeNode]
            for childNode in maxOutDegreeChildren:
                if self.isInCycle_ChildDirection(childNode):
                    return [maxOutDegreeNode, childNode]

        if maxInDegree == 1 and maxOutDegree == 1:
            return edges[-1]

        return []
    
    def isInCycle_ParentDirection(self, node: int):
        startNode = node
        while True:
            if self.parent[node]:
                node = self.parent[node][0]
                if node == startNode:
                    return True
            else:
                return False

    def isInCycle_ChildDirection(self, node: int):
        startNode = node
        while True:
            if self.child[node]:
                node = self.child[node][0]
                if node == startNode:
                    return True
            else:
                return False


if __name__ == "__main__":
    testCases = [([[1, 2], [1, 3], [2, 3]], [2, 3]),
                 ([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]], [4, 1]),
                 ([[2, 1], [3, 1], [4, 2], [1, 4]], [2, 1])]
    for i, testCase in enumerate(testCases):
        edges, ans = testCase
        tic = time.time()
        ret = Solution().findRedundantDirectedConnection(edges)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
