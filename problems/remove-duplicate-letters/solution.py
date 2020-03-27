import time
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """Greedy algorithm, recursively find smallest letter from left"""
        if not s:
            return ''

        letters = Counter(s)
        leftSmallestLetterIndex = 0
        for i, letter in enumerate(s):
            letters[letter] -= 1
            if letter < s[leftSmallestLetterIndex]:
                leftSmallestLetterIndex = i
            if letters[letter] == 0:
                break
        curLetter = s[leftSmallestLetterIndex]
        # remove all duplicate curLetter and recursive for greedy search in right string
        return curLetter + self.removeDuplicateLetters(s[leftSmallestLetterIndex:].replace(curLetter, ''))


if __name__ == "__main__":
    testCases = [("bcabc", "abc"), ("cbacdcbc", "acdb"), ("baab", "ab"), ("bddbccd", "bcd")]
    for i, testCase in enumerate(testCases):
        s, ans = testCase
        tic = time.time()
        ret = Solution().removeDuplicateLetters(s)
        toc = time.time()
        print(f"{i}: {ret == ans}, return {ret} in {toc-tic:.3f}s.")