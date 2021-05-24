DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
class Solution:
    # Approach1: DFS + visited. easy to get stack overflow, not recommended for interview
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        visited = set()
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if self.is_valid(grid, i, j, visited):
                    # visited.add((i, j))
                    self.dfs(grid, i, j, visited)
                    ans += 1
        return ans
    
    # mark all valid 1
    def dfs(self, grid, x, y, visited):
        visited.add((x, y))
        for dx, dy in DIRECTIONS:
            _x, _y = dx + x, dy + y
            if self.is_valid(grid, _x, _y, visited):
                self.dfs(grid, _x, _y, visited)

    def is_valid(self, grid, x, y, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] == '0':
            return False
        if (x, y) in visited:
            return False
        return True
    
    # Approach2: use stack to minic dfs so it won't stack overflow
    def dfs2(self, grid, x, y, visited):
        stack = [(x, y)]
        visited.add((x, y))
        while stack:
            nx, ny = stack.pop()
            for dx, dy in DIRECTIONS:
                _x, _y = dx + nx, dy + ny
                if self.is_valid(grid, _x, _y, visited):
                    visited.add((_x, _y))
                    stack.append((_x, _y))
                    
    # Approach3: BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        visited = set()
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if self.is_island(grid, i, j, visited):
                    self.bfs(grid, i, j, visited)
                    ans += 1
        return ans
    
    def bfs(self, grid, i, j, visited):
        q = collections.deque([(i, j)])
        while q:
            x, y = q.popleft()
            for dx, dy in DIRECTIONS:
                _x, _y = x + dx, y + dy
                if self.is_island(grid, _x, _y, visited):
                    q.append((_x, _y))
                    visited.add((_x, _y))
    
    def is_island(self, grid, i, j, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return False
        if (i, j) in visited:
            return False
        if grid[i][j] != '1':
            return False
        return True

# APP3: union find
# 10:23
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind()
        # init
        for i in range(m):
            for j in range(n):
                if self.is_valid(grid, i, j):
                    uf.parent[(i, j)] = (i, j)
                    uf.size += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue
                for dx, dy in DIRECTIONS:
                    _x, _y = i + dx, j + dy
                    if self.is_valid(grid, _x, _y):
                        uf.union((i, j), (_x, _y))
        return uf.size

    def is_valid(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] != "1":
            return False
        return True


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = 0

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            self.size -= 1
            self.parent[p_x] = self.parent[p_y]

    def find(self, x):
        node = x
        while node != self.parent[node]:
            node = self.parent[node]

        cur = x
        while cur != node:
            self.parent[cur] = node
            cur = self.parent[cur]
        return node
