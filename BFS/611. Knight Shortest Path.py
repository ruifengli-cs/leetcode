"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        if not grid or not grid[0] or grid[destination.x][destination.y]:
            return -1
        if source.x == destination.x and source.y == destination.y:
            return 0
        m, n = len(grid), len(grid[0])

        start_q = collections.deque([(source.x, source.y)])
        start_visited = {(source.x, source.y): 0}
        end_q = collections.deque([(destination.x, destination.y)])
        end_visited = {(destination.x, destination.y): 0}

        while start_q and end_q:
            distance = self.extend_q(start_q, start_visited, end_visited, grid)
            if distance != -1:
                return distance
            distance = self.extend_q(end_q, end_visited, start_visited, grid)
            if distance != -1:
                return distance
        return -1

    def extend_q(self, q, visited, opposite_vis, grid):
        size = len(q)
        for i in range(size):
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                _x, _y = x + dx, y + dy
                if self.is_valid(grid, _x, _y, visited):
                    q.append((_x, _y))
                    visited[(_x, _y)] = visited[(x, y)] + 1
                    if (_x, _y) in opposite_vis:
                        return visited[(_x, _y)] + opposite_vis[(_x, _y)]
        return -1

    def is_valid(self, grid, x, y, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] == 1:
            return False
        if (x, y) in visited:
            return False
        return True
