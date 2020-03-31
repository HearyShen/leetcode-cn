import time
from typing import List


class UnionFindSet:
    def __init__(self):
        self.parents = {}

    def find(self, x):
        """Find x's tree's root"""
        self.parents.setdefault(x, x)  # if not exist, set as x itself
        if x != self.parents[x]:
            # compress path, set the parent of all the tree-nodes to root node
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        """Set x's tree's parent to y's tree's root."""
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parents[x_root] = y_root
            return True
        else:
            # if x and y are already in the same set (tree), 
            # then union operation shall not be proceeded (redundant union).
            return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """Solve with Union-Find Set (aka `DSU`) by finding redundant union"""
        if not edges:
            return []

        ufs = UnionFindSet()
        for edge in edges:
            if not ufs.union(edge[0], edge[1]):
                # if the union operation of u and v are not proceeded,
                # then this edge is a redundant connection.
                return edge
        return []


if __name__ == "__main__":
    testCases = [([[1, 2], [1, 3], [2, 3]], [2, 3]),
                 ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4])]
    for i, testCase in enumerate(testCases):
        edges, ans = testCase
        tic = time.time()
        ret = Solution().findRedundantConnection(edges)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
