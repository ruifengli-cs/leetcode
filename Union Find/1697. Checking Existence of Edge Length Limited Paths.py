# APP1: for one query, we need to know all edges within limit.
# for all queries, sort queries by limit, sort edge by weight.
# Time: O(nlgn) space: O(n)
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = sorted([(p, q, l, i) for i, (p, q, l) in enumerate(queries)], key=lambda q: q[2])
        edgeList.sort(key=lambda e: e[2])

        uf = UnionFind(n)

        ans = [None] * len(queries)
        idx = 0
        for p, q, limit, i in queries:
            while idx < len(edgeList) and edgeList[idx][2] < limit:
                u, v, w = edgeList[idx]
                uf.union(u, v)
                idx += 1
            ans[i] = uf.find(p) == uf.find(q)
        return ans


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, u, v):
        self.parent[self.find(u)] = self.find(v)

    def find(self, u):
        node = u
        while node != self.parent[node]:
            node = self.parent[node]

        cur = u
        while cur != node:
            self.parent[cur] = node
            cur = self.parent[cur]
        return node