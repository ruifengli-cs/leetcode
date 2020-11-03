class Solution:
    # APP1: dfs to min path sum from (i, j) to end. ans dfs(grid, i, j)
    # Time: O(2^n) space: O(m + n) Time: TLE
    #     def minPathSum(self, grid: List[List[int]]) -> int:
    #         if not grid or not grid[0]:
    #             return 0
    #         return self.dfs(grid, 0, 0)

    #     def dfs(self, grid, i, j):
    #         if i == len(grid) - 1 and j == len(grid[0]) - 1:
    #             return grid[-1][-1]
    #         res = sys.maxsize
    #         if i + 1 < len(grid):
    #             res = min(res, self.dfs(grid, i + 1, j))
    #         if j + 1 < len(grid[0]):
    #             res = min(res, self.dfs(grid, i, j + 1))
    #         return grid[i][j] + res

    #     APP2: dfs + memoization
    #     Time: O(n^2) space: O(n^2) Runtime: 19%
    #     def minPathSum(self, grid: List[List[int]]) -> int:
    #         if not grid or not grid[0]:
    #             return 0
    #         memo = {}
    #         return self.dfs(grid, 0, 0, memo)

    #     def dfs(self, grid, i, j, memo):
    #         if i == len(grid) - 1 and j == len(grid[0]) - 1:
    #             return grid[-1][-1]
    #         if i == len(grid) or j == len(grid[0]):
    #             return sys.maxsize
    #         if (i, j) in memo:
    #             return memo[(i, j)]
    #         memo[(i, j)] = grid[i][j] + min(self.dfs(grid, i + 1, j, memo), self.dfs(grid, i, j + 1, memo))
    #         return memo[(i, j)]

    #     APP3: DP. f[i][j]: min path sum from start to (i, j)
    #     f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j]
    #     ans: f[m][n]. init: f[0][0] = 0
    #     Time: O(n^2) space: O(n^2) Runtime: 99%
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        f = [[sys.maxsize] * (n + 1) for _ in range(m + 1)]
        f[0][1] = f[1][0] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = grid[i - 1][j - 1] + min(f[i - 1][j], f[i][j - 1])
        return f[-1][-1]

#         [[0, 0, x, x],
#          [0, 1, 3, 1],
#          [x, 1, 6, 2],
#          [x, 4, 6, 3]]

#         [[1,3,1],
#          [1,5,1],
#          [4,2,1]]


#     APP4: DP. one dimemsion array optimization.
#     TIme: O(n^2) space: O(n)
