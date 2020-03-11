import time
from typing import List

class Solution:
    @staticmethod
    def isSegValid(seg: str) -> bool:
        if len(seg) > 1:
            return seg[0] != '0' and int(seg) in range(256)
        elif len(seg) == 1:
            return True
        else:
            return False

    @staticmethod
    def isValid(segs: List[str]) -> bool:
        isValids = [Solution.isSegValid(seg) for seg in segs]
        return all(isValids)

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:   # if invalid
            return []

        ipAddrs = set()
        validLen = [1,2,3]
        for lenA in validLen:
            for lenB in validLen:
                if lenA + lenB > len(s):
                    break
                for lenC in validLen:
                    if lenA + lenB + lenC > len(s):
                        break
                    for lenD in validLen:
                        if lenA + lenB + lenC + lenD == len(s):
                            segA, segB, segC, segD = s[:lenA], s[lenA:lenA+lenB], s[lenA+lenB:lenA+lenB+lenC], s[lenA+lenB+lenC:]
                            segs = [segA, segB, segC, segD]
                            if Solution.isValid(segs):
                                ipAddr = '.'.join([seg for seg in segs])
                                ipAddrs.add(ipAddr)
                            break
        return list(ipAddrs)
        


if __name__ == "__main__":
    testCases = [("25525511135", ["255.255.11.135", "255.255.111.35"]), ("010010", ["0.10.0.10","0.100.1.0"]), ("101023", ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])]

    for i, testCase in enumerate(testCases):
        digits, ans = testCase
        tic = time.time()
        ret = Solution().restoreIpAddresses(digits)
        toc = time.time()
        print(f"{i}: {set(ret) == set(ans)}, {ret} in {toc-tic:.3f}s.")