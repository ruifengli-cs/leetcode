# APP1: union find for all connected elements. then compare counter for those connected components
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # init
        n = len(source)
        parent = [i for i in range(n)]

        # union all the components
        for x, y in allowedSwaps:
            self.union(x, y, parent)
        components = defaultdict(list)
        for i in range(n):
            components[self.find(i, parent)].append(i)

        # get actual num instead of index, calculate res
        res = 0
        for comps in components.values():
            A = [source[i] for i in comps]
            B = [target[i] for i in comps]
            res += sum((Counter(A) - Counter(B)).values())
        return res

    def union(self, x, y, parent):
        parent[self.find(x, parent)] = self.find(y, parent)

    def find(self, x, parent):
        node = parent[x]
        while node != parent[node]:
            node = parent[node]

        cur = x
        while cur != parent[cur]:
            cur, parent[cur] = parent[cur], node
        return node