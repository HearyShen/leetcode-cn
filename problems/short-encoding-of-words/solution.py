import time
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        encWords = set(words)
        
        # if there is a word same as the current word's suffix, discard it
        for word in words:
            for i in range(1, len(word)):
                if word[i:] in encWords:
                    encWords.discard(word[i:])
        
        return sum(len(encWord)+1 for encWord in encWords)  # add 1 for ending mark '#'


if __name__ == "__main__":
    words = ["time", "me", "bell"]

    tic = time.time()
    ret = Solution().minimumLengthEncoding(words)
    toc = time.time()

    print(f"Found min len: {ret} in {toc-tic:.3f}s.")