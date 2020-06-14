DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    # APP1: BFS. Find all 0s, enqueue, then pop to add all 1s.
    # # Time: O(n * m) Space: O(n * m)
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return [[]]
        n, m = len(matrix), len(matrix[0])
        q = collections.deque()
        visited = {}
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    visited[(i, j)] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                _x, _y = x + dx, y + dy
                if (_x, _y) not in visited and 0 <= _x < n and 0 <= _y < m:
                    q.append((_x, _y))
                    visited[(_x, _y)] = visited[(x, y)] + 1
                    res[_x][_y] = visited[(x, y)] + 1
        return res

    # APP2: DP: f[i][j] = min(f[i - 1][j], f[i + 1][j], f[i][j - 1], f[i][j + 1]) + 1 if matrix[i][j] != 0
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return [[]]
        n, m = len(matrix), len(matrix[0])
        f = [[n * m] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    f[i][j] = 0
                    continue
                if i > 0:
                    f[i][j] = min(f[i][j], f[i - 1][j] + 1)
                if j > 0:
                    f[i][j] = min(f[i][j], f[i][j - 1] + 1)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if matrix[i][j] == 0:
                    continue
                if i < n - 1:
                    f[i][j] = min(f[i][j], f[i + 1][j] + 1)
                if j < m - 1:
                    f[i][j] = min(f[i][j], f[i][j + 1] + 1)
        return f
