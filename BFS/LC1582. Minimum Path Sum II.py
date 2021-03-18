DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    """
    @param matrix: a matrix
    @return: the minimum height
    """

    # Attemp1: NOT WORKING since 4 directions you will have dead loop using dfs
    # dfs. return min path sum.
    # Time: O(4^n) space: O(n^2)

    # def minPathSumII(self, matrix):
    #     if not matrix:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #     return self.dfs(matrix, m - 1, 0)

    # def dfs(self, matrix, i, j):
    #     if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
    #         return sys.maxsize
    #     if i == 0 and j == len(matrix[0]) - 1:
    #         return matrix[i][j]
    #     return matrix[i][j] + min(self.dfs(matrix, i + 1, j), self.dfs(matrix, i - 1, j), self.dfs(matrix, i, j + 1), self.dfs(matrix, i, j - 1))

    # APP1: dp + dfs. f[i][j]:min path sum from (n - 1, 0) to (i, j)
    # dfs: fill dp f[i][j]. from 4 directions. if out boundary or matrix[_i][_j] + cursum >= f[_i][_j], continue.
    # Time: O(4^n) with pruning. Space: O(n^2)
    def minPathSumII(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        f = [[sys.maxsize] * len(matrix[0]) for _ in range(len(matrix))]
        self.dfs(matrix, len(matrix) - 1, 0, matrix[-1][0], f)
        return f[0][-1]

    def dfs(self, matrix, i, j, cursum, f):
        f[i][j] = cursum
        for dx, dy in DIRECTIONS:
            x, y = i + dx, j + dy
            if self.is_valid(matrix, x, y, cursum, f):
                self.dfs(matrix, x, y, matrix[x][y] + cursum, f)

    def is_valid(self, matrix, x, y, cursum, f):
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
            return False
        if cursum + matrix[x][y] >= f[x][y]:
            return False
        return True

    # APP2: bfs. enqueue adjacent pos. reenter queue when dis < previous
    # Time: O(4^n) space: O(n^2)
    def minPathSumII(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        q, visited = collections.deque([(m - 1, 0)]), {(m - 1, 0): matrix[m - 1][0]}
        while q:
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                _x, _y = x + dx, y + dy
                if self.is_valid(matrix, _x, _y, visited, x, y):
                    q.append((_x, _y))
                    visited[(_x, _y)] = matrix[_x][_y] + visited[(x, y)]
        return visited[(0, n - 1)]

    def is_valid(self, matrix, x, y, visited, pre_x, pre_y):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return False
        if (x, y) in visited and (visited[(x, y)] <= visited[(pre_x, pre_y)] + matrix[x][y]):
            return False
        return True

    # Attempt2: DP: f: min path sum.
    # NOT WOKRING FOR [[0,0,0,1,1],[0,1,0,0,0],[0,1,1,1,1], [0,1,1,1,1]]
    # f[i][j] = matrix[i][j] + min(f[i][j - 1], f[i][j + 1], f[i - 1][j], f[i + 1][j])
    # we can do two pass DP.
    # Time: O(n^2) space: O(n^2)
    # def minPathSumII(self, matrix):
    #     if not matrix or not matrix[0]:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])
    #     f = [[sys.maxsize] * (n + 2) for _ in range(m + 2)]
    #     f[-1][1] = f[-2][0] = 0
    #     for i in range(1, m + 1):
    #         for j in range(n, 0, -1):
    #             f[i][j] = min(f[i][j], matrix[i - 1][j - 1] + min(f[i - 1][j], f[i][j + 1]))
    #     print(f)
    #     for i in range(m, 0, -1):
    #         for j in range(1, n + 1):
    #             f[i][j] = matrix[i - 1][j - 1] + min(f[i][j - 1], f[i + 1][j])
    #     print(f)
    #     return f[1][-2]

    # APP4: bfs