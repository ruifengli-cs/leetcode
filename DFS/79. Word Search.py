DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0, set()):
                    return True
        return False

    def dfs(self, board, x, y, word, i, visited):
        ch_board, ch = board[x][y], word[i]
        if ch_board != ch:
            return False
        if i == len(word) - 1:
            return True
        visited.add((x, y))
        for dx, dy in DIRECTIONS:
            _x, _y = x + dx, y + dy
            if _x < 0 or _x >= len(board) or _y < 0 or _y >= len(board[0]) or (_x, _y) in visited:
                continue
            if self.dfs(board, _x, _y, word, i + 1, visited):
                return True
        visited.remove((x, y))
        return False