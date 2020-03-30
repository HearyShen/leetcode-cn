import time
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # TODO: 2020.3.19
        if not board:
            return 
        yLen, xLen = len(board), len(board[0])

        # traverse and start DFS search
        for yIdx in range(1, yLen-1):
            for xIdx in range(1, xLen-1):
                if board[yIdx][xIdx] == 'O':
                    self.dfsModify(yIdx, xIdx, board)
    
    def dfsModify(self, yIdx, xIdx, board):
        """Modify surrounded 'O' with DFS search"""
        if yIdx not in range(len(board)) or xIdx not in range(len(board[0])):
            return False

        if board[yIdx][xIdx] == 'X':
            return True
        else:
            board[yIdx][xIdx] = 'X'         # set X as default when entering O to avoid infinite search loop
            up = self.dfsModify(yIdx-1, xIdx, board)
            down = self.dfsModify(yIdx+1, xIdx, board)
            left = self.dfsModify(yIdx, xIdx-1, board)
            right = self.dfsModify(yIdx, xIdx+1, board)
            if up and down and left and right:
                # board[yIdx][xIdx] = 'X'   # keep X if surrounded
                return True
            else:
                board[yIdx][xIdx] = 'O'     # restore O if not surrounded
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