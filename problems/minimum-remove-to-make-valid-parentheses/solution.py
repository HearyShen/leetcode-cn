import time


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        idxStack = []
        pStack = []
        chars = list(s)
        for i, char in enumerate(chars):
            if char in {'(', ')'}:
                if pStack and char == ')' and pStack[-1] == '(':
                    idxStack.pop()
                    pStack.pop()
                else:
                    idxStack.append(i)
                    pStack.append(char)
        
        idxSet = set(idxStack)
        # print(idxStack)
        return ''.join([chars[i] for i in range(len(chars)) if i not in idxSet])

        

if __name__ == "__main__":
    testCases = [("lee(t(c)o)de)", "lee(t(c)o)de"), ("a)b(c)d", "ab(c)d"), ("))((", ""), ("(a(b(c)d)", "a(b(c)d)")]

    for i, testCase in enumerate(testCases):
        s, ans = testCase
        tic = time.time()
        ret = Solution().minRemoveToMakeValid(s)
        toc = time.time()
        print(f"{i}: {ret == ans}, {ret} in {toc-tic:.3f}s.")