import time
from typing import List


class Solution(object):
    def kthSmallestPrimeFraction(self, primes, K):
        from fractions import Fraction
        def under(x):
            r"""
            $$
            \frac{A_m}{A_{n+1}} < \frac{A_m}{A_n} < \frac{A_{m+1}}{A_{n+1}}
            $$
            """
            # Return the number of fractions below x,
            # and the largest such fraction
            count = best = 0
            i = -1
            for j in range(1, len(primes)):
                while primes[i+1] < primes[j] * x:
                    i += 1
                count += i+1
                if i >= 0:
                    best = max(best, Fraction(primes[i], primes[j]))
            return count, best

        # Binary search for x such that there are K fractions
        # below x.
        lo, hi = 0.0, 1.0
        while hi - lo > 1e-9:
            mi = (lo + hi) / 2.0
            count, best = under(mi)
            if count < K:
                lo = mi
            else:
                ans = best
                hi = mi

        return [ans.numerator, ans.denominator]


if __name__ == "__main__":
    testCases = [([1, 2, 3, 5], 3, [2, 5]), ([1, 7], 1, [1, 7])]
    for i, testCase in enumerate(testCases):
        A, K, ans = testCase
        tic = time.time()
        ret = Solution().kthSmallestPrimeFraction(A, K)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")