import time
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Use BFS to find the shortest coin change path."""
        if amount == 0:
            return 0

        bfsQueue = []
        for coin in coins:
            bfsQueue.append([coin])

        while bfsQueue:
            curPath = bfsQueue[0]
            
            curSum = sum(curPath)
            if curSum == amount:
                # print(curPath)
                return len(curPath)
            elif curSum > amount:
                pass    # do nothing, no bfsQueue add
            else:
                # find nexts
                for coin in coins:
                    if curSum + coin <= amount:
                        bfsQueue.append(curPath + [coin])

            bfsQueue.remove(bfsQueue[0])
        return -1


if __name__ == "__main__":
    testcases = [([1, 2, 5], 11, 3), ([1], 0, 0), ([1,2,5], 100, 20)]

    for i, testcase in enumerate(testcases):
        coins, amount, ans = testcase
        print(f"{i}: {testcase}")
        tic = time.time()
        ret = Solution().coinChange(coins, amount)
        toc = time.time()
        print(f"{i}: {ret == ans} ({ret}) in {toc-tic:.3f}s.")