DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


class Solution:
    # APP1: crush function crushes candies and return false if no candy to crush. O(mn)
    # drop funciton reshape grid to stable. O(mn)
    # Time: O(mn) space: O(mn)
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board or not board[0]:
            return [[]]
        while self.crush_candy(board):
            self.drop(board)
        return board

    def crush_candy(self, board):
        crushed_any = False
        m, n = len(board), len(board[0])
        visited = {}
        for i in range(m):
            for j in range(n):
                if self.mark(board, i, j):
                    crushed_any = True
        self.crush(board)
        return crushed_any

    def drop(self, board):
        m, n = len(board), len(board[0])
        for j in range(n):
            s = e = m - 1
            while e >= 0:
                while s >= 0 and board[s][j] != 0:
                    s -= 1
                e = s - 1
                while e >= 0 and board[e][j] == 0:
                    e -= 1
                if e >= 0:
                    board[s][j], board[e][j] = board[e][j], board[s][j]
                    s -= 1
                    e -= 1

    def mark(self, board, i, j):
        marked_any = False
        if (i + 2) < len(board) and abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]) != 0:
            board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
            marked_any = True

        if (j + 2) < len(board[0]) and abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]) != 0:
            board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
            marked_any = True

        return marked_any

    def crush(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] < 0:
                    board[i][j] = 0