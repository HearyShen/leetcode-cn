import time
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        self.seenCells = {}
        todayCells = cells
        today = 0
        cycle = None
        while today < N:
            cellsTuple = tuple(todayCells)  # convert to tuple (hashable)
            try:
                lastSeenDay = self.seenCells[cellsTuple]
            except KeyError:
                self.seenCells[cellsTuple] = today
            else:
                cycle = today - lastSeenDay
                if N - today > cycle:  # if room to skip
                    today += (
                        (N - today) // cycle) * cycle  # then skip K-cycles
                    continue  # IMPORTANT

            print(f"{today}/{N}: {todayCells}")
            todayCells = self.findNextDay(todayCells)
            today += 1

        return todayCells

    def findNextDay(self, cells: List[int]):
        return [
            int(cellID > 0 and cellID < len(cells) - 1
                and cells[cellID - 1] == cells[cellID + 1])
            for cellID in range(len(cells))
        ]


if __name__ == "__main__":
    testcases = [([1, 0, 0, 0, 1, 0, 0, 1], 99, [0, 0, 1, 0, 1, 0, 0, 0])]

    for i, testcase in enumerate(testcases):
        print(f"{i}: {testcase}")
        cells, N, correctAns = testcase
        tic = time.time()
        ret = Solution().prisonAfterNDays(cells, N)
        toc = time.time()
        print(f"{i}: {ret==correctAns}\t({ret}) in {toc-tic:.3f}s.")