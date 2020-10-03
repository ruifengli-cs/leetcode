DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        if not grid or not grid[0]:
            return []
        m, n, visited_1, visited_2, res = len(grid), len(grid[0]), set(), set(), set()
        q1, q2 = collections.deque(), collections.deque()
        # initialization
        for j in range(n):
            q1.append((0, j, grid[0][j]))
            visited_1.add((0, j))
            q2.append((m - 1, j, grid[m - 1][j]))
            visited_2.add((m - 1, j))
        for i in range(m):
            q1.append((i, 0, grid[i][0]))
            visited_1.add((i, 0))
            q2.append((i, n - 1, grid[i][n - 1]))
            visited_2.add((i, n - 1))

        # double bfs
        while q1 or q2:
            if q1:
                x1, y1, v1 = q1.popleft()
                if (x1, y1) in visited_2:
                    res.add((x1, y1))
                for dx, dy in DIRECTIONS:
                    _x1, _y1 = x1 + dx, y1 + dy
                    if self.is_valid(grid, _x1, _y1, v1, visited_1):
                        # print(x1, y1, _x1, _y1)
                        q1.append((_x1, _y1, grid[_x1][_y1]))
                        visited_1.add((_x1, _y1))
            if q2:
                x2, y2, v2 = q2.popleft()
                if (x2, y2) in visited_1:
                    res.add((x2, y2))
                for dx, dy in DIRECTIONS:
                    _x2, _y2 = x2 + dx, y2 + dy
                    if self.is_valid(grid, _x2, _y2, v2, visited_2):
                        q2.append((_x2, _y2, grid[_x2][_y2]))
                        visited_2.add((_x2, _y2))
        final_res = []
        for x, y in res:
            final_res.append([x, y])
        return final_res

    def is_valid(self, grid, x, y, v_old, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        if grid[x][y] < v_old:
            return False
        return True