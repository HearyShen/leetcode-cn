import time
from typing import List
from collections import defaultdict


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        yesterday2today = defaultdict(list)

        cellsYesterday = [-1] + cells + [-1]
        for day in range(N):
            cellsToday = yesterday2today[tuple(cellsYesterday)]
            if not cellsToday:
                cellsToday = [-1] + [
                    int(cellsYesterday[cellID - 1] == cellsYesterday[cellID + 1])
                    for cellID in range(1,
                                        len(cellsYesterday) - 1)
                ] + [-1]
                yesterday2today[tuple(cellsYesterday)] = cellsToday
            cellsYesterday = cellsToday
        return cellsToday[1:-1]

if __name__ == "__main__":
    cells = [0, 1, 0, 1, 1, 0, 0, 1]
    N = 7000000

    tic = time.time()
    ret = Solution().prisonAfterNDays(cells, N)
    toc = time.time()

    print(f"Caulated {N} days prison situation:\n{ret}\nin {toc-tic:.3f}s.")