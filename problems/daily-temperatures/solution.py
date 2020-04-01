import time
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # TODO: 2020.4.1
        if not T:
            return []
        
        deltaDays = [0] * len(T)
        stack = []
        for i in range(len(T)):
            # print([(i, T[i]) for i in stack], (i, T[i]))
            if not stack:
                stack.append(i)
                continue
            # record and pop all the colder days in stack
            j = len(stack) - 1
            while j >= 0 and T[stack[j]] < T[i]:
                deltaDays[stack[j]] = i - stack[j]
                stack.pop()
                j -= 1
            stack.append(i)
        return deltaDays


if __name__ == "__main__":
    testCases = [([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])]
    for i, testCase in enumerate(testCases):
        temperatures, ans = testCase
        tic = time.time()
        ret = Solution().dailyTemperatures(temperatures)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")
