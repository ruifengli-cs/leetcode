IS_WORD = '#'
DIRECTIONS = [(0, -1), (0, 1), (1, 0), (-1, 0)]


class Solution:

    #     APP1: brute force
    #     for each word, traverse through board to find first matching ch, then dfs
    #     Time: O(m * n * 4 ^ k + k * N), k = len(word). Space: O(1)

    #     APP2: use trie to store board
    #     traverse trought board, for each ch, traverse through board to add . But we don't know when to end.

    #     APP3: use trie to store words
    #     traverse through words, add word to trie.
    #     loop through board and see if ch in trie, then dfs
    #     Time: O(m * n * 4 ^ k + k * N) space: O(k * N) Runtime: 46%

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        # build trie
        trie, m, n, res = {}, len(board), len(board[0]), []
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node[IS_WORD] = True
        # Search in board
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    self.dfs(board, i, j, trie, res, [board[i][j]], set([(i, j)]))
        return res

    def dfs(self, board, i, j, trie, res, path, visited):
        if IS_WORD in trie[board[i][j]]:
            res.append(''.join(path))
            del trie[board[i][j]][IS_WORD]
        for dx, dy in DIRECTIONS:
            _x, _y = i + dx, j + dy
            if self.is_valid(board, _x, _y, trie[board[i][j]], visited):
                path.append(board[_x][_y])
                visited.add((_x, _y))
                self.dfs(board, _x, _y, trie[board[i][j]], res, path, visited)
                visited.remove((_x, _y))
                path.pop()

    def is_valid(self, board, i, j, trie, visited):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] not in trie:
            return False
        if (i, j) in visited:
            return False
        return True
