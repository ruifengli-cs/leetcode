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


# DP: f[i][j]: max profit at ith day at state j.
# j has 5 states total. 1: not bought, 2: bought first, 3:sold first, 4: bought second, 5: sold second
# function: f[i][2] = max(f[i - 1][1], f[i - 1][2] + prices[i - 1] - prices[i - 2])
# f[i][3/5] = max(f[i - 1][3], f[i - 1][2] + prices[i - 1] - prices[i - 2])
# for state 4, you can be 2 on i - 1th day and to stat 3-4, on i th day.
# f[i][4] = max(f[i - 1][1], f[i - 1][4] + prices[i - 1] - prices[i - 2], f[i - 1][2] + prices[i - 1] -  prices[i - 2 n])
# init: f[0][1] = 0, f[0][i] = -max
# Time: O(n) space: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        f = [[-sys.maxsize] * 6 for _ in range(n + 1)]
        f[0][1] = 0
        for i in range(1, n + 1):
            for j in range(1, 6, 2):
                # f[i][3/5] = max(f[i - 1][3], f[i - 1][2] + prices[i - 1] - prices[i - 2])
                f[i][j] = f[i - 1][j]
                if j > 1 and f[i - 1][j - 1] != -sys.maxsize:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + prices[i - 1] - prices[i - 2])

            for j in range(2, 5, 2):
                # f[i][4] = max(f[i - 1][1], f[i - 1][4] + prices[i - 1] - prices[i - 2], f[i - 1][2] + prices[i - 1] -  prices[i - 2 n])
                f[i][j] = f[i - 1][j - 1]
                if f[i - 1][j] != -sys.maxsize:
                    f[i][j] = max(f[i][j], f[i - 1][j] + prices[i - 1] - prices[i - 2])
                if j > 2 and f[i - 1][j - 2] != -sys.maxsize:
                    f[i][j] = max(f[i][j], f[i - 1][j - 2] + prices[i - 1] - prices[i - 2])
        return max(f[n][1], f[n][3], f[n][5])