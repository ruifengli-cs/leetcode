# app1: dfs, for each house, we have 3 options to paint. can't pick prev color.
# dfs: return min cost if choose color i for cur idx
# Time: O(2^n) space: O(n) stack runtime: TLE
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        return self.dfs(costs, 0, -1)

    def dfs(self, costs, idx, prev_color):
        if idx == len(costs):
            return 0
        cost = sys.maxsize
        for i in range(3):
            if i == prev_color:
                continue
            cost = min(cost, self.dfs(costs, idx + 1, i) + costs[idx][i])
        return cost


# APP2: dp. f[i][j] min cost till house i if paint color j to house i.
# f[i][j] = min(f[i - 1][k]) + costs[i][j] for all k != j.
# ans: min(f[n])
# init: f[0][j] = 0
# Time: O(n) space: O(n)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        m, n = len(costs), len(costs[0])

        f = [[sys.maxsize] * n for _ in range(m + 1)]
        f[0][0] = f[0][1] = f[0][2] = 0

        for i in range(1, m + 1):
            for j in range(n):
                # f[i][j] = costs[i - 1][j]
                for k in range(3):
                    if k == j:
                        continue
                    f[i][j] = min(f[i][j], f[i - 1][k] + costs[i - 1][j])
        return min(f[m])


# APP3: optimize it using one dimention array.
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        m, n = len(costs), len(costs[0])
        old = [0] * n
        new = [sys.maxsize] * n

        for i in range(m):
            for j in range(n):
                new[j] = sys.maxsize
                for k in range(n):
                    if k == j:
                        continue
                    new[j] = min(new[j], old[k] + costs[i][j])
            new, old = old, new
        return min(old)


