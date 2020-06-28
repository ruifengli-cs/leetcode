class Solution:
    # APP1: Recursion definition: p(i,j): minimum path sum from i, j to the bottom
    # p(i, j) = min(p(i + 1, j) + p(i + 1, j + 1)) + t[i][j]
    # Time: O(2^n) space: O(1) where n = len(t) Runtime: TLE
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        f, n = triangle[:], len(triangle)
        if n == 1:
            return triangle[0][0]
        return self.dfs(triangle, 0, 0, n)

    def dfs(self, t, i, j, n):
        if i == n:
            return 0
        return min(self.dfs(t, i + 1, j, n), self.dfs(t, i + 1, j + 1, n)) + t[i][j]

    #     APP2: recursion + memoization.
    #     Time: O(N) space: O(N) N = number of element in t Runtime: 56%
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        f, n = triangle[:], len(triangle)
        if n == 1:
            return triangle[0][0]
        return self.dfs(triangle, 0, 0, n, {})

    def dfs(self, t, i, j, n, memo):
        if i == n:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        memo[(i, j)] = min(self.dfs(t, i + 1, j, n, memo), self.dfs(t, i + 1, j + 1, n, memo)) + t[i][j]
        return memo[(i, j)]

    #     APP3: DP definition f[i][j]: minimum path sum from i, j to the bottom
    #     f[i][j] =  min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]
    #     Time: O(N) space: O(N) N = number of element in t. Runtime: 90%

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        f, n = triangle[:], len(triangle)
        if n == 1:
            return triangle[0][0]
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                f[i][j] += min(f[i + 1][j], f[i + 1][j + 1])
        return f[0][0]

    # APP4: DP + rolling array
    # Time: O(n) space: O(n) n = len(t[-1]) Runtime: 77%
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        f, n = triangle[-1][:], len(triangle)
        if n == 1:
            return triangle[0][0]
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                f[j] = min(f[j], f[j + 1]) + triangle[i][j]
        return f[0]