# APP1: dfs to try all combo and find the minimum.
# Time: O(k * (k - 1)^(n - 1)) space: O(n)

# APP2: DP
# defination: f[i][j]: min cost paint till house i ending with color j.
# function: f[i][j] = cost[i][j] + min(f[i - 1][p]) where 0 <= p <= k and p != j
# init: f[0][j] = 0
# ans: min(f[n]), n = len(cost)
# Time: O(nk^2) space: O(nk) runtime: 9%
# class Solution:
#     def minCostII(self, costs: List[List[int]]) -> int:
#         if not costs:
#             return 0
#         n, k = len(costs), len(costs[0])

#         # init
#         f = [[sys.maxsize] * k for _ in range(n)]
#         for j in range(k):
#             f[0][j] = costs[0][j]

#         for i in range(1, n):
#             for j in range(k):
#                 for p in range(k):
#                     if p == j:
#                         continue
#                     f[i][j] = min(f[i][j], costs[i][j] + f[i - 1][p])
#         return min(f[n - 1])

# APP3: dp optimization with min1, min2.
# # Time: O(nk) space: O(nk) Runtime: 78%
# class Solution:
#     def minCostII(self, costs: List[List[int]]) -> int:
#         if not costs:
#             return 0
#         n, k = len(costs), len(costs[0])

#         # init
#         f = [[sys.maxsize] * k for _ in range(n + 1)]
#         for j in range(k):
#             f[0][j] = 0

#         idx1 = idx2 = 0
#         for i in range(1, n + 1):
#             # find min1 and min2 from i - 1 row
#             min1, min2 = sys.maxsize, sys.maxsize
#             for j in range(k):
#                 if f[i - 1][j] < min1:
#                     min2, idx2, min1, idx1 = min1, idx1, f[i - 1][j], j
#                 elif f[i - 1][j] < min2:
#                     min2, idx2 = f[i - 1][j], j

#             # update i row, use idx1 instead of min1 to avoid [[8]] data
#             for j in range(k):
#                 if j != idx1:
#                     f[i][j] = costs[i - 1][j] + f[i - 1][idx1]
#                 else:
#                     f[i][j] = costs[i - 1][j] + f[i - 1][idx2]
#         return min(f[n])

# APP4. dp optimize space using one dimension array.
# Time: O(nk) space: O(nk) Runtime: 95%
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n, k = len(costs), len(costs[0])

        # init
        old = [0] * k
        new = [sys.maxsize] * k

        idx1 = idx2 = 0
        for i in range(1, n + 1):
            # find min1 and min2 from i - 1 row
            min1, min2 = sys.maxsize, sys.maxsize
            for j in range(k):
                if old[j] < min1:
                    min2, idx2, min1, idx1 = min1, idx1, old[j], j
                elif old[j] < min2:
                    min2, idx2 = old[j], j

            # update i row, use idx1 instead of min1 to avoid [[8]] data
            for j in range(k):
                if j != idx1:
                    new[j] = costs[i - 1][j] + old[idx1]
                else:
                    new[j] = costs[i - 1][j] + old[idx2]
            new, old = old, new
        return min(old)



