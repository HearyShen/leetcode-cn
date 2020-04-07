import time


class Solution:
    """Solved with BFS"""
    @staticmethod
    def isValid(r, c, k):
        r_digits = [int(d) for d in str(r)]
        c_digits = [int(d) for d in str(c)]
        return sum(r_digits) + sum(c_digits) <= k


    def movingCount(self, m: int, n: int, k: int) -> int:
        if m == 0 and n == 0 or k < 0:
            return 0

        count = 0
        visited = {(0, 0)}
        bfsQueue = [(0, 0)]
        while bfsQueue:
            r, c = bfsQueue.pop(0)
            count += 1
            nextRCs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            validNextRCs = [(r, c) for r, c in nextRCs if 0<=r<m and 0<=c<n and Solution.isValid(r,c,k) and (r,c) not in visited]
            bfsQueue.extend(validNextRCs)
            visited.update(validNextRCs)
        return count


if __name__ == "__main__":
    testCases = [(2,3,1,3), (3,1,0,1), (5,4,0,1), (11,8,16,88)]
    for i, testCase in enumerate(testCases):
        m, n, k, ans = testCase
        tic = time.time()
        ret = Solution().movingCount(m, n, k)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")