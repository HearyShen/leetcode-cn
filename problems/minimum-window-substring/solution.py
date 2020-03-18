import time

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        l, r = 0, 0
        minWindowLen = len(s)
        targetChars = set(list(t))
        while r <= len(s):
            curChars = set(list(s[l:r]))
            print(curChars)
            if targetChars - curChars:
                # if still need to match
                r += 1
            else:
                # if all found
                # shrink the left border
                for newL in range(l, r):
                    if targetChars - set(list(s[newL:r])):
                        l = newL - 1
                        if r-l <= minWindowLen:
                            minWindowLen = r-l
                            minWindowStr = s[l:r]
                        l = newL
                        break
        return minWindowStr

        

if __name__ == "__main__":
    testCases = [("ADOBECODEBANC", "ABC", "BANC"), ("a", "a", "a")]
    for i, testCase in enumerate(testCases):
        S, T, ans = testCase
        tic = time.time()
        ret = Solution().minWindow(S, T)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")