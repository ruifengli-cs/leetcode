# APP1: generate squares that up to n. dfs to pick squares like backpack.
# each time we can pick one of
# Time: O(sqrt(n) ^ n) space: O(n) Runtime: TLE at 43
class Solution:
    def numSquares(self, n: int) -> int:
        if not n or n < 0:
            return
        squares = [i * i for i in range(1, n + 1) if i * i <= n]
        # print(squares)
        return self.dfs(squares, n)

    def dfs(self, squares, n):
        if n < 0:
            return -1
        if n == 0:
            return 0
        count = sys.maxsize
        for i in range(len(squares)):
            if squares[i] <= n:
                temp = self.dfs(squares, n - squares[i])
                if temp == -1:
                    break
                count = min(count, temp + 1)
        return count if count != sys.maxsize else -1

# APP2: dfs + memoization.
# Time: O(n* sqrt(n)) sapce: O(n * sqrt(n)) Runtime: TLE at 8609
class Solution:
    def numSquares(self, n: int) -> int:
        if not n or n < 0:
            return
        squares = [i * i for i in range(1, n + 1) if i * i <= n]
        memo = {}
        return self.dfs(squares, n, memo)

    def dfs(self, squares, n, memo):
        if n < 0:
            return -1
        if n == 0:
            return 0
        count = sys.maxsize
        if n in memo:
            return memo[n]
        for i in range(len(squares)):
            if squares[i] <= n:
                temp = self.dfs(squares, n - squares[i], memo)
                if temp == -1:
                    break
                count = min(count, temp + 1)
        memo[n] = count if count != sys.maxsize else -1
        return memo[n]

# APP3: dp. f[i]: least number of perfect square which sum to i
# f[i] = min(f[i - square[j]]) + 1 for all square[j] < i. ans = f[n]
# Time: O(n * sqrt(n)) space: o(n * sqrt(n)) runtime: 12%
# start time: 12:21 end: 12:31. duratio++ n: 10min
class Solution:
    def numSquares(self, n: int) -> int:
        if not n or n < 0:
            return
        squares = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        f = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            j = 0
            while j < len(squares) and squares[j] <= i:
                f[i] = min(f[i], f[i - squares[j]] + 1)
                j += 1
        return f[n]
