# APP1: if only allow once. for each prices[i], we need to know it's previous minimum. then get max while loop through the list.
# if only allow twice, then use array to store left, then do a pass from the right.
# Time: O(n) space: O(n) Runtime: 48%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n, profits, res, left_min, right_max, left_best, right_best = len(prices), [], 0, prices[0], prices[-1], 0, 0
        # left to right pass
        for i in range(n):
            profit = prices[i] - left_min
            left_best = max(left_best, profit)
            profits.append(left_best)
            left_min = min(left_min, prices[i])
            res = max(left_best, res)
        # right to left pass
        for i in range(n - 1, -1, -1):
            profit = right_max - prices[i]
            right_best = max(right_best, profit)
            res = max(res, profits[i] + right_best)
            right_max = max(right_max, prices[i])
        return res