import time


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """BFS with DP"""
        n = len(word1)
        m = len(word2)

        # if word1 or word2 is empty, the distance is m+n
        if n * m == 0:
            return n + m

        # DP matrix
        # D[i][j] represents minDistance between word1[:i] and word2[:j]
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # init border states in DP matrix
        # the distance between a k-len word and another 0-len word is always k
        # (simply by removing or inserting k characters)
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # finish the whole DP matrix in buttom-up way.
        # there are 3 ways to edit word1[:i] to word2[:j]
        # 1. add a letter to word1[:i-1] -> word2[:j] 's solution
        # 2. add a letter to word1[:i] -> word2[:j-1] 's solution
        # 3. change a letter to word1[:i-1] -> word2[j-1] 's solution if word1[i-1] != word2[j-1]
        # take the min value of the 3 ways as min distance from word1[:i] to word2[:j]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]


if __name__ == "__main__":
    testCases = [("horse", "ros", 3), ("intention", "execution", 5)]
    for i, testCase in enumerate(testCases):
        word1, word2, ans = testCase
        tic = time.time()
        ret = Solution().minDistance(word1, word2)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")