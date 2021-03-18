# APP1: Union find
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if not positions:
            return []
        res = []
        grid = [[0] * n for _ in range(m)]
        uf = UnionFind()
        for x, y in positions:
            if grid[x][y]:
                res.append(uf.size)
                continue
            grid[x][y] = 1
            uf.size += 1
            uf.parent[(x, y)] = (x, y)
            for dx, dy in DIRECTIONS:
                _x, _y = x + dx, y + dy
                if self.is_valid(grid, _x, _y):
                    uf.union((x, y), (_x, _y))
            res.append(uf.size)
        return res

    def is_valid(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if grid[x][y] == 0:
            return False
        return True


class UnionFind:
    def __init__(self):
        self.size = 0
        self.parent = {}

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            self.size -= 1
            self.parent[p_x] = p_y

    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]

        node = x
        while node != root:
            self.parent[node] = root
            node = self.parent[node]
        return root
