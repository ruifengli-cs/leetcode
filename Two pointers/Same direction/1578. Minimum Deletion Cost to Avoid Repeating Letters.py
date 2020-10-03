class Solution:
    # APP1: two pointers
    # Time: O(n) space: O(1) Runtime: 85%
    def minCost(self, s: str, cost: List[int]) -> int:
        if not s or not cost:
            return 0
        res, n, start = 0, len(s), 0
        while start < n - 1:
            end, max_val, summ = start + 1, cost[start], cost[start]
            while end < n and s[start] == s[end]:
                max_val = max(max_val, cost[end])
                summ += cost[end]
                end += 1
            res += summ - max_val
            start = end
        return res