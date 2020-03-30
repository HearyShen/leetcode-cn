import time
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        yLen, xLen = len(board), len(board[0])
        self.isChecked = [[False for x in range(xLen)] for y in range(yLen)]    # record checked ones to prune search space

        # traverse and start DFS search
        for yIdx in range(1, yLen-1):
            for xIdx in range(1, xLen-1):
                if not self.isChecked[yIdx][xIdx] and board[yIdx][xIdx] == 'O':
                    modified = set()    # record modified ones (presumed as X)
                    isSurrounded = self.dfsModify(yIdx, xIdx, board, modified)
                    if not isSurrounded:    # if not surrounded, restore O for all modified
                        for y, x in modified:
                            board[y][x] = 'O'
    
    def dfsModify(self, yIdx, xIdx, board, modified: set):
        """Modify surrounded 'O' with DFS search"""
        if yIdx not in range(len(board)) or xIdx not in range(len(board[0])):
            return False

        if board[yIdx][xIdx] == 'X':
            return True
        else:
            board[yIdx][xIdx] = 'X'         # presume X when entering O to avoid infinite search loop
            modified.add((yIdx, xIdx))
            self.isChecked[yIdx][xIdx] = True
            # if up, down, left, right are all surrounded (use cascade if-and to prune search space)
            if self.dfsModify(yIdx-1, xIdx, board, modified) \
                and self.dfsModify(yIdx+1, xIdx, board, modified) \
                    and self.dfsModify(yIdx, xIdx-1, board, modified) \
                        and self.dfsModify(yIdx, xIdx+1, board, modified):
                # board[yIdx][xIdx] = 'X'   # keep X if surrounded
                return True
            else:
                board[yIdx][xIdx] = 'O'     # restore O if not surrounded
                modified.remove((yIdx, xIdx))
                return False


if __name__ == "__main__":
    testCases = [(
        [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        ,
        [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X']
        ]
    ),
    (
        [
            ["O","X","X","O","X"],
            ["X","O","O","X","O"],
            ["X","O","X","O","X"],
            ["O","X","O","O","O"],
            ["X","X","O","X","O"]
        ],
        [
            ["O","X","X","O","X"],
            ["X","X","X","X","O"],
            ["X","X","X","O","X"],
            ["O","X","O","O","O"],
            ["X","X","O","X","O"]
        ]
    )]
    for i, testCase in enumerate(testCases):
        board, ans = testCase
        tic = time.time()
        Solution().solve(board)
        toc = time.time()
        format_board = '\n'.join([' '.join(xLine) for xLine in board])
        print(f"{i}: {board == ans}, return \n{format_board}\n in {toc-tic:.3f}s.")