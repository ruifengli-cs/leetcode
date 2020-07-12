class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        n = len(board)
        r_set, c_set, box_set = [set() for _ in range(n)], [set() for _ in range(n)], [set() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ch = board[i][j]
                box_idx = 3 * (i // 3) + j // 3
                if ch != '.':
                    r_set[i].add(ch)
                    c_set[j].add(ch)
                    box_set[box_idx].add(ch)
        self.dfs(board, 0, r_set, c_set, box_set, n)

    def dfs(self, board, idx, r_set, c_set, box_set, n):
        i, j = idx // 9, idx % 9
        ch = board[i][j]
        box_idx = 3 * (i // 3) + j // 3
        if ch != '.':
            if i == n - 1 and j == n - 1:
                return True
            if self.dfs(board, idx + 1, r_set, c_set, box_set, n):
                return True
            return False
        for k in range(1, 10):
            if self.is_valid(board, i, j, str(k), r_set[i], c_set[j], box_set[box_idx]):
                board[i][j] = str(k)
                r_set[i].add(str(k))
                c_set[j].add(str(k))
                box_set[box_idx].add(str(k))
                if i == n - 1 and j == n - 1:
                    return True
                if self.dfs(board, idx + 1, r_set, c_set, box_set, n):
                    return True
                board[i][j] = '.'
                r_set[i].remove(str(k))
                c_set[j].remove(str(k))
                box_set[box_idx].remove(str(k))
        return False

    def is_valid(self, board, i, j, k, r_set, c_set, box_set):
        if k in r_set or k in c_set or k in box_set:
            return False
        return True
