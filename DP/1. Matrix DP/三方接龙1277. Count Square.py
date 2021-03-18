# APP1: f[i][j]: count squares ending with (i, j).
# f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
# Time: O(mn) space: O(mn) Runtime: 58%
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == 0:
                    continue
                f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
        return sum([sum(i) for i in f])






