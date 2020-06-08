# input: n * m matrix of 0 and 1
# each cell, which can be 0 or 1, find the distance of nearest 0
# number of cells within 10k, at least one 0.

[
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 0]
]

[
    [4, 3, 2],
    [3, 2, 1],
    [2, 1, 0]
]

# f[i][j] = if any of matrix[i - 1][j], matrix[i + 1][j], matrix[i][j + 1], matrix[i][j - 1] is 0, then f[i][j] = 1

if matrix[i][j] == 0, then f[i][j] == 0
f[i][j] = min(f[i - 1][j], f[i + 1][j], f[i][j + 1], f[i][j - 1]) + 1

if matrix[i - 1][j] == 0:
    f[i][j] = f[i - 1][j]

q = [(0, 1), (1, 2), (2, 1), (2, 2)]
for (1, 0), when I pop out (0, 1), distance is 2
but
when
I
pop
out(2, 0), distance is less
# output: matrix
# [
# [1,0,1],
# [2,1,0],
# [1,0,0]
# ]

O(n * n * n * n)

# approach1: for each cell, do bfs till finding the 0, if it's 0, then return 0.
# approach2: find all 0s and enqueue them, then do bfs for all 0s, and mark 1 for the distance.

import collections

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def find_nearest_zero(matrix):
        if not matrix or not matrix[0]:
            return [[]]
        n, m = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                distance = self.bfs(matrix, i, j)
                if distance != -1:
                    res[i][j] = distance
        return res

    def bfs(self, matrix, i, j):
        if matrix[i][j] == 0:
            return 0
        q = collections.deque([(i, j)])
        visited = set([(i, j)])
        distance = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if matrix[x][y] == 0:
                    return distance
                for dx, dy in DIRECTIONS:
                    _x, _y = x + dx, y + dy
                    if self.is_valid(matrix, _x, _y, visited):
                        q.append((_x, _y))
                        visited.add((_x, _y))
            distance += 1
        return -1

    def is_valid(self, matrix, x, y, visited):
        if x < 0 and x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return False

        if (x, y) in visited:
            return False

        return True



