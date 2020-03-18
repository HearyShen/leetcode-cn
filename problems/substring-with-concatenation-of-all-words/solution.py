import time
from typing import List

class Solution:
    def isValidStr(self, ascWords: List[str], s: str) -> bool:
        wordLen, wordCount = len(ascWords[0]), len(ascWords)
        sWords = sorted([s[wordLen*i:wordLen*i+wordLen] for i in range(int(len(s)/wordLen))])
        return ascWords == sWords

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        firstWords = set(words)
        ascWords = sorted(words)
        wordLen, wordCount = len(words[0]), len(words)
        strLen = wordLen * wordCount
        validIndexes = []
        for i in range(len(s) - strLen + 1):
            curWord = s[i:i+wordLen]
            if curWord in firstWords:
                possibleStr = s[i:i+strLen]
                if self.isValidStr(ascWords, possibleStr):
                    validIndexes.append(i)
        return validIndexes


if __name__ == "__main__":
    testCases = [("barfoothefoobarman", ["foo","bar"], [0,9]), ("wordgoodgoodgoodbestword", ["word","good","best","word"], [])]

    for i, testCase in enumerate(testCases):
        s, words, ans = testCase
        tic = time.time()
        ret = Solution().findSubstring(s, words)
        toc = time.time()
        print(f"{i}: {set(ret) == set(ans)}， return {ret} in {toc-tic:.3f}s.")
