import time
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        l, r = 0, 0
        minWindowLen = len(s)
        minWindowStr = ""
        targetChars = Counter(t)
        curChars = Counter(s[l:r])
        while r <= len(s):
            # print(curChars)
            if targetChars - curChars:
                # if still need to match
                r += 1
                # print(r)
                if r <= len(s):
                    curChars[s[r-1]] += 1
            else:
                # if all found
                # shrink the left border
                if r - l <= minWindowLen:  # if the raw str is min
                    minWindowLen = r - l
                    minWindowStr = s[l:r]
                for newL in range(l+1, r+1):  # if the shrinked str is min
                    curChars[s[newL-1]] -= 1 
                    if targetChars - curChars:
                        l = newL - 1
                        curChars[s[l]] += 1
                        if r - l < minWindowLen:
                            minWindowLen = r - l
                            minWindowStr = s[l:r]
                        break
                l = l + 1  # whether shrinked or not, move window to find next
                curChars[s[l-1]] -= 1
        return minWindowStr


if __name__ == "__main__":
    testCases = [("ADOBECODEBANC", "ABC", "BANC"), ("a", "a", "a"),
                 ("a", "aa", ""), ("ab", "b", "b")]
    for i, testCase in enumerate(testCases):
        S, T, ans = testCase
        tic = time.time()
        ret = Solution().minWindow(S, T)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")