class Solution:
    # APP1: dfs + recursion
    # Time: O(2^n) space: O(m + n)

    # APP2: dp f: from start to (i, j) unique paths. ans: f[m - 1][n - 1]
    # f[i][j] = f[i - 1][j] + f[i][j - 1] if grid[i][j] != 1 else 0
    # Time: O(mn) space: O(n) runtime: 70%
    # 这题bug很多，第14行初始化一定要判断对
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        f = [0] * (n + 1)
        f[1] = 1 if grid[0][0] != 1 else 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1] == 1:
                    f[j] = 0
                    continue
                f[j] += f[j - 1]
        return f[-1]