class Solution:
    # APP1: DFS. Time: 2 ^ (n*m) space: O(1) Runtime: TLE
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dfs(m, n, 0, 0)

    def dfs(self, m, n, x, y):
        if x > m - 1 or y > n - 1:
            return 0
        if x == m - 1 and y == n - 1:
            return 1
        return self.dfs(m, n, x + 1, y) + self.dfs(m, n, x, y + 1)

    # APP2: DFS + memoization Time: O(n * m) Space: O(n * m) Runtime: 90%
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {(m - 1, n - 1): 1}
        self.dfs(m, n, memo, 0, 0)
        return memo[(0, 0)]

    def dfs(self, m, n, memo, x, y):
        if x > m - 1 or y > n - 1:
            return 0
        if (x, y) in memo:
            return memo[(x, y)]
        memo[(x, y)] = self.dfs(m, n, memo, x + 1, y) + self.dfs(m, n, memo, x, y + 1)
        return memo[(x, y)]

    # APP3: DP
    # 1. f[i][j]: how many possible path to reach [n-1][m-1] from i,j
    # 2. f[i][j] = f[i + 1][j] + f[i][j + 1], i + 1, j + 1 within boundry
    # 3. initialization: f[n-1][m - 1] = 1
    # 4. Time: O(m*n) Space: O(m*n)  Runtime: 90%
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0] * n for _ in range(m)]
        f[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    f[i][j] += f[i + 1][j]
                if j + 1 < n:
                    f[i][j] += f[i][j + 1]
        return f[0][0]

    # Optimize above method using single array instead of matrix
    # Time: O(m * n) Space: O(n) Runtime: 90%
    def uniquePaths(self, m: int, n: int) -> int:
        f = [1] * n
        for _ in range(m - 1):
            for j in range(n - 2, -1, -1):
                f[j] += f[j + 1]
        return f[0]

    # APP4:
    # 1. f[i][j]: how many possible path to reach i, j from 0, 0
    # 2. f[i][j] = f[i - 1][j] + f[i][j - 1]
    # 3. Initialization: f[0][0] = 1, ans = f[m - 1][n - 1]
    # 4. Time: O(m*n) space: O(m*n) Runtime: 90%
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0] * n for _ in range(m)]
        f[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    f[i][j] += f[i - 1][j]
                if j > 0:
                    f[i][j] += f[i][j - 1]
        return f[m - 1][n - 1]

        # Optimize above method using one dimension array
        # Time: O(nm) space: O(n) Runtime: 94%
    def uniquePaths(self, m: int, n: int) -> int:
        f = [1] * n
        for _ in range(m - 1):
            for j in range(1, n):
                f[j] += f[j - 1]
        return f[n - 1]






