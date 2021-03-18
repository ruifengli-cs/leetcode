# 1:44
# APP1: BFS.
class Solution:
    def canFinish(self, n: int, courses: List[List[int]]) -> bool:
        if not n or n < 0:
            return False
        data = self.get_data(courses)
        indegrees = self.get_indegrees(courses, n)
        q = collections.deque()
        count = 0

        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)
                count += 1
        while q:
            node = q.popleft()
            for nei in data[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    q.append(nei)
                    count += 1
        return count == n

    def get_data(self, courses):
        res = collections.defaultdict(list)
        for c1, c2 in courses:
            res[c1].append(c2)
        return res

    def get_indegrees(self, courses, n):
        res = [0] * n
        for c1, c2 in courses:
            res[c2] += 1
        return res
