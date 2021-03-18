# APP1: iterate matrix for bomb pos, for each pos, use two pointer count enemies.
# Time: O(mn * max(m, n)), space: O(1)

# APP2: dp.
# def: f[i][j]: max enemies you can kill placing bomb at (i, j)
# f[i][j] = up[i - 1][j] + left[i][j - 1] + right[i][j + 1] + down[i + 1][j] | grid[i][j] == 0
# we can reuse the same matrix f for 4 directions.
# Runtime: O(n^2) space: O(n^2)
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n, final = len(grid), len(grid[0]), 0
        f = [[0] * n for _ in range(m)]
        res = [[0] * n for _ in range(m)]
        # up
        for i in range(m):
            for j in range(n):
                f[i][j] = 0
                if grid[i][j] == 'W':
                    continue
                else:
                    if grid[i][j] == 'E':
                        f[i][j] = 1
                    if i > 0:
                        f[i][j] += f[i - 1][j]
                res[i][j] += f[i][j]
        # down
        for i in range(m - 1, -1, -1):
            for j in range(n):
                f[i][j] = 0
                if grid[i][j] == 'W':
                    continue
                else:
                    if grid[i][j] == 'E':
                        f[i][j] = 1
                    if i < m - 1:
                        f[i][j] += f[i + 1][j]
                res[i][j] += f[i][j]

        # left
        for i in range(m):
            for j in range(n):
                f[i][j] = 0
                if grid[i][j] == 'W':
                    continue
                else:
                    if grid[i][j] == 'E':
                        f[i][j] = 1
                    if j > 0:
                        f[i][j] += f[i][j - 1]
                res[i][j] += f[i][j]

        # right
        for i in range(m):
            for j in range(n - 1, -1, -1):
                f[i][j] = 0
                if grid[i][j] == 'W':
                    continue
                else:
                    if grid[i][j] == 'E':
                        f[i][j] = 1
                    if j < n - 1:
                        f[i][j] += f[i][j + 1]
                res[i][j] += f[i][j]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0' and res[i][j] > final:
                    final = res[i][j]
        return final
