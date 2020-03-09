import time
from typing import List


class Solution:
    def __init__(self):
        self.leastCoinsDP = {}  # {amount: leastCoins}

    def coinChange(self, coins: List[int], amount: int) -> int:
        """Use BFS to find the shortest coin change path."""
        coinsHigh2Small = sorted(coins, reverse=True)
        return self.dfsCoinChange(coinsHigh2Small, amount)

    def dfsCoinChange(self, coins: List[int], amount) -> int:
        if amount == 0:
            return 0
        elif amount < 0:
            return -1
        else:
            try:
                leastCoin = self.leastCoinsDP[amount]
            except KeyError:
                subPlans = [
                    self.dfsCoinChange(coins, amount - coin) for coin in coins
                ]
                if max(subPlans) >= 0:
                    self.leastCoinsDP[amount] = min([
                        plan + 1 for plan in subPlans if plan >= 0
                    ])  # add the current coin (plan+1)
                else:
                    self.leastCoinsDP[amount] = -1
                return self.leastCoinsDP[amount]
            else:
                return leastCoin


if __name__ == "__main__":
    testcases = [([1, 2, 5], 11, 3), ([1], 0, 0), ([1, 2, 5], 100, 20),
                 ([186, 419, 83, 408], 6249, 20)]

    for i, testcase in enumerate(testcases):
        coins, amount, ans = testcase
        print(f"{i}: {testcase}")
        tic = time.time()
        ret = Solution().coinChange(coins, amount)
        toc = time.time()
        print(f"{i}: {ret == ans} ({ret}) in {toc-tic:.3f}s.")