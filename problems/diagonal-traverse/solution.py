from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rLen, cLen = len(matrix), len(matrix[0])
        r, c = 0, 0
        outs = []
        up = True
        while 0 <= r < rLen and 0 <= c < cLen:
            outs.append(matrix[r][c])
            if up:              # moving up-right
                if r - 1 < 0:       # out up bound
                    if c + 1 < cLen:    # in right bound
                        c += 1
                    else:               # out right bound
                        r += 1
                    up = False
                elif c + 1 >= cLen: # out right bound
                    r += 1
                    up = False
                else:               # in matrix
                    r -= 1
                    c += 1
            else:               # moving left-down
                if c - 1 < 0:       # out left bound
                    if r + 1 < rLen:    # in down bound
                        r += 1
                    else:               # out down bound
                        c += 1
                    up = True
                elif r + 1 >= rLen: # out down bound
                    c += 1
                    up = True
                else:               # in matrix
                    c -= 1
                    r += 1
        return outs
