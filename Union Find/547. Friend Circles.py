class Solution:
    # APP1: dfs: for each person, dfs mark all his friends in visited set.
    # Time: O(n^2) Space: O(n^2) Runtime: 5%
        def findCircleNum(self, M: List[List[int]]) -> int:
            if not M or not M[0]:
                return 0
            m, n, visited, count = len(M), len(M[0]), set(), 0
            for i in range(m):
                if (i, i) not in visited:
                    self.dfs(M, i, visited, n)
                    count += 1
            return count

        def dfs(self, M, i, visited, n):
            for j in range(n):
                if i == j:
                    visited.add((i, j))
                    continue
                if M[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    self.dfs(M, j, visited, n)

    # APP2: bfs: for each person, add all his friends into queue and mark them.
    # Time: O(n^2) Space: O(n^2) Runtim: 5%
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0
        count, m, n, visited = 0, len(M), len(M[0]), set()
        for i in range(m):
            if (i, i) not in visited:
                self.bfs(M, i, visited, n)
                count += 1
        return count

    def bfs(self, M, i, visited, n):
        q = collections.deque([(i, i)])
        visited.add((i, i))
        while q:
            x, y = q.popleft()
            for j in range(n):
                if y == j:
                    visited.add((y, j))
                    continue
                if M[y][j] == 1 and (y, j) not in visited:
                    q.append((y, j))
                    visited.add((y, j))

    # APP3: union find: union all friends, return how many circle
    # Time: O(n^2) Space: O(n^2) Runtime: 43
class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """

    def findCircleNum(self, M):
        if not M or not M[0]:
            return 0
        n = len(M)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 0:
                    continue
                uf.union(i, j)
        return uf.size


class UnionFind():
    def __init__(self, n):
        self.size = n
        self.parent = {}
        for i in range(n):
            self.parent[i] = i

    def union(self, i, j):
        parent1, parent2 = self.find(i), self.find(j)
        if parent1 != parent2:
            self.size -= 1
            self.parent[parent1] = parent2

    def find(self, i):
        root = i
        while root != self.parent[root]:
            root = self.parent[root]

        while i != root:
            i, self.parent[i] = self.parent[i], root
        return root