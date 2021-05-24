class Solution:
    # APP1: for each row, try dfs. visited = {'col': set(), 'sum': set(), 'diff': set()}
    # Time: O(n^n) space: O(n^2) runtime: 74%
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n or n < 0:
            return []
        res, visited = [], {'col': set(), 'sum': set(), 'diff': set()}
        self.dfs(n, res, 0, [], visited)
        return res

    def dfs(self, n, res, row, queens, visited):
        if row == n:
            res.append(self.draw(queens))
        for j in range(n):
            if self.is_valid(row, j, visited):
                queens.append(j)
                visited['col'].add(j)
                visited['sum'].add(row + j)
                visited['diff'].add(row - j)
                self.dfs(n, res, row + 1, queens, visited)
                visited['diff'].remove(row - j)
                visited['sum'].remove(row + j)
                visited['col'].remove(j)
                queens.pop()

    def is_valid(self, row, j, visited):
        if j in visited['col'] or (row + j) in visited['sum'] or (row - j) in visited['diff']:
            return False
        return True

    def draw(self, queens):
        res, n = [], len(queens)
        for num in queens:
            res.append('.' * num + 'Q' + '.' * (n - num - 1))
        return res