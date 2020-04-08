import time
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # TODO: 2020.4.9
        pass


if __name__ == "__main__":
    testCases = [([[1],[2],[3],[]], True), ([[1,3],[3,0,1],[2],[0]], False)]
    for i, testCase in enumerate(testCases):
        rooms, ans = testCase
        tic = time.time()
        ret = Solution().canVisitAllRooms(rooms)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")