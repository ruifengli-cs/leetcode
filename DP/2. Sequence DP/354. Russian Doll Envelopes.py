class Solution:
    # APP1: brute force. sort the envelopes, for each, we can pick or not pick. Pick the valid ones.
    # Time: O(2^n) space: O(n) Runtime: TLE
    #     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    #         if not envelopes:
    #             return 0
    #         envelopes.sort()
    #         return self.dfs(envelopes, 0, 0, 0)

    #     def dfs(self, envelopes, i, w, h):
    #         if i == len(envelopes):
    #             return 0
    #         temp = self.dfs(envelopes, i + 1, w, h)
    #         if envelopes[i][0] > w and envelopes[i][1] > h:
    #             temp = max(temp, self.dfs(envelopes, i + 1, envelopes[i][0], envelopes[i][1]) + 1)
    #         return temp

    # APP2: dfs + memoization
    # Time: O(n^2) space: O(n^2) runtime: TLE
    #     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    #         if not envelopes:
    #             return 0
    #         envelopes.sort()
    #         memo = {}
    #         return self.dfs(envelopes, 0, (0, 0), memo)

    #     def dfs(self, envelopes, i, size, memo):
    #         if i == len(envelopes):
    #             return 0
    #         if (i, size) in memo:
    #             return memo[(i, size)]
    #         temp = self.dfs(envelopes, i + 1, size, memo)
    #         if envelopes[i][0] > size[0] and envelopes[i][1] > size[1]:
    #             temp = max(temp, self.dfs(envelopes, i + 1, (envelopes[i][0], envelopes[i][1]), memo) + 1)
    #         memo[(i, size)] = temp
    #         return temp

    # APP3: DP. sort w in ascending order. loop through envelopes,
    # f[i]: max number of envelopes you can get till envelope i.
    # f[i] = max(f[j]) where j < i and wj < wi and hj < hi
    # Time: O(n^2) space: O(n^2) Runtime: TLE
    # def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    #     if not envelopes:
    #         return 0
    #     envelopes.sort()
    #     n = len(envelopes)
    #     f = [0] + [1] * n
    #     for i in range(1, n + 1):
    #         for j in range(i):
    #             if envelopes[j - 1][0] < envelopes[i - 1][0] and envelopes[j - 1][1] < envelopes[i - 1][1]:
    #                 f[i] = max(f[i], f[j] + 1)
    #     return max(f)

    # APP4: sort w in ascending order. when w1 == w2, we want to pick h1 and repalce h1 with h2 if needed.
    # so we need to sort h in descending order. then the question becomes find LIS for h.
    # [2,3],[5,4],[6,4],[6,7]
    # Time: O(nlgn) space: O(1) Runtime: 99.9%
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        f = []
        for w, h in envelopes:
            if not f or h > f[-1]:
                f.append(h)
                continue
            pos = bisect.bisect_left(f, h)
            f[pos] = h
        return len(f)





