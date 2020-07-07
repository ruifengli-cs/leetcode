class Solution:
    # APP1: dfs: for each person, dfs mark all his friends in visited set.
    # Time: O(n^2) Space: O(n^2) Runtime: 5%
    #     def findCircleNum(self, M: List[List[int]]) -> int:
    #         if not M or not M[0]:
    #             return 0
    #         m, n, visited, count = len(M), len(M[0]), set(), 0
    #         for i in range(m):
    #             if (i, i) not in visited:
    #                 self.dfs(M, i, visited, n)
    #                 count += 1
    #         return count

    #     def dfs(self, M, i, visited, n):
    #         for j in range(n):
    #             if i == j:
    #                 visited.add((i, j))
    #                 continue
    #             if M[i][j] == 1 and (i, j) not in visited:
    #                 visited.add((i, j))
    #                 self.dfs(M, j, visited, n)

    # APP2: bfs: for each person, add all his friends into queue and mark them.
    # Time: O(n^2) Space: O(n^2) Runtim:
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
        while q:
            x, y =
        for j in range(n):
            if i == j:
                visited.add((i, j))
                continue
            if M[i][j] == 1 and (i, j) not in visited:
                q.append((i, j))

    # APP3: union find: union all friends, return how many circle
    # Time: O(n^2) Space: O(n^2)
    # def findCircleNum(self, M: List[List[int]]) -> int:
