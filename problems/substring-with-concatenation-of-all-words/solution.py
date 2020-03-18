import time
from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        firstWords = set(words)
        wordsCounter = Counter(words)
        wordLen, wordCount = len(words[0]), len(words)
        strLen = wordLen * wordCount
        validIndexes = []
        for i in range(len(s) - strLen + 1):
            if s[i:i + wordLen] in firstWords:
                possibleStr = s[i:i + strLen]
                wordsCounterOfS = Counter([possibleStr[i:i + wordLen] for i in range(0, len(possibleStr), wordLen)])
                if wordsCounter == wordsCounterOfS:
                    validIndexes.append(i)
        return validIndexes


if __name__ == "__main__":
    testCases = [("barfoothefoobarman", ["foo", "bar"], [0, 9]),
                 ("wordgoodgoodgoodbestword", ["word", "good", "best",
                                               "word"], [])]

    for i, testCase in enumerate(testCases):
        s, words, ans = testCase
        tic = time.time()
        ret = Solution().findSubstring(s, words)
        toc = time.time()
        print(f"{i}: {set(ret) == set(ans)}， return {ret} in {toc-tic:.3f}s.")
