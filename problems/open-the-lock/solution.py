import time
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        deadends = set(deadends)

        if not target or start in deadends:
            return -1

        visited = {start}
        step = 0
        bfsQueue = [start]
        while bfsQueue:
            for _ in range(len(bfsQueue)):
                curNode = bfsQueue.pop(0)
                if curNode == target:
                    return step
                
                for i in range(len(curNode)):
                    curNum = int(curNode[i])
                    nextNumR = (curNum + 1) % 10
                    nextNumL = (curNum - 1) % 10
                    for nextNum in [nextNumR, nextNumL]:
                        nextNode = curNode[0:i] + str(nextNum) + curNode[i+1:]
                        if nextNode not in visited and nextNode not in deadends:
                            bfsQueue.append(nextNode)
                            visited.add(nextNode)
            step += 1
        return -1


if __name__ == "__main__":
    testCases = [
        (["0201", "0101", "0102", "1212", "2002"], "0202", 6),
        (["8888"], "0009", 1),
        (["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888", -1), 
        (["0000"], "8888", -1)
    ]
    for i, testCase in enumerate(testCases):
        deadends, target, ans = testCase
        tic = time.time()
        ret = Solution().openLock(deadends, target)
        toc = time.time()
        print(f"{i}: {ret==ans}, return {ret} in {toc-tic:.3f}s.")
