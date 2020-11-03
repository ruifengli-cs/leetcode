class Solution:
    """
    @param n: the row of the matrix
    @param m: the column of the matrix
    @param after: the matrix
    @return: restore the matrix
    """
    # after[i][j] = after[i - 1][j] + after[i][j - 1] + before[i][j] - after[i - 1][j - 1]
    # so before[i][j] = after[i][j] + after[i - 1][j - 1] - after[i - 1][j] - after[i][j - 1]
    def matrixRestoration(self, n, m, after):
        if not n or not m or not after:
            return [[]]
        before = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                before[i][j] = after[i][j]
                if i > 0 and j > 0:
                    before[i][j] += after[i - 1][j - 1]
                if i > 0:
                    before[i][j] -= after[i - 1][j]
                if j > 0:
                    before[i][j] -= after[i][j - 1]
        return before