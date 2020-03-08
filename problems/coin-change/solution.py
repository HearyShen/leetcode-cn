import time
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Use BFS to find the shortest coin change path."""
        coinsHigh2Small = sorted(coins, reverse=True)
        return self.dfsCoinChange(coinsHigh2Small, [], amount)

    def dfsCoinChange(self, coins: List[int], plan: List[int], amount: int) -> int:
        sumCoins = sum(plan)
        if sumCoins == amount:
            print(f"Found {plan}.")
            return len(plan)
        elif sumCoins > amount:
            return -1
        else:
            for coin in coins:
                retSum = self.dfsCoinChange(coins, plan + [coin], amount)
                if retSum > 0:      # if found, then return to root, else, ignore it.
                    return retSum
        return -1


if __name__ == "__main__":
    testcases = [([1, 2, 5], 11, 3), ([1], 0, 0), ([1, 2, 5], 100, 20), ([186,419,83,408], 6249, 26)]

    for i, testcase in enumerate(testcases):
        coins, amount, ans = testcase
        print(f"{i}: {testcase}")
        tic = time.time()
        ret = Solution().coinChange(coins, amount)
        toc = time.time()
        print(f"{i}: {ret == ans} ({ret}) in {toc-tic:.3f}s.")