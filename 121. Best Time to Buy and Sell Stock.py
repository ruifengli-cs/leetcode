class Solution:
# APP1: find all buy&sell days combination and keep updating best benefit
# Time: O(n^2) Space: O(1). Runtime: TLE
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #     n = len(prices)
    #     max_profit = -sys.maxsize
    #     for i in range(n - 1):
    #         # you're allowed to buy&sell on the same day 
    #         for j in range(i, n):
    #             max_profit = max(max_profit, prices[j] - prices[i])
    #     return max_profit

# APP2: for each buy date, Pre-calculate the largest sell date. 
# Time: O(n), Space: O(n), Runtime: 40%, memory: 5%
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #     n = len(prices)
    #     suffix = [0] * n
    #     largest, ans = prices[n - 1], -sys.maxsize
    #     for i in range(n - 1, -1, -1):
    #         largest = max(largest, prices[i])
    #         suffix[i] = largest
    #     for i in range(n):
    #         ans = max(ans, suffix[i] - prices[i])
    #     return ans 
                
# APP3: for each sell day, Pre-calculate the lowest buy date before. 
# Time: O(n), Space: O(n), Runtime: 63% memory: 5%
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #     n = len(prices)
    #     prefix = [0] * n 
    #     lowest, ans = prices[0], -sys.maxsize
    #     for i in range(n):
    #         lowest = min(lowest, prices[i])
    #         prefix[i] = lowest
    #     for i in range(n):
    #         ans = max(ans, prices[i] - prefix[i])
    #     return ans
        
# APP4-Draft: DP: f[i][j]: max profit buy at i and sell at j using two dimension array 
# Here we can calculate f[i][j] directly using prices[j] = prices[i], which means we don't need two dimension 
# f[i][j] = max(f[i][j - 1] + price[j] - price[j - 1], price[j] - price[i] if i == j - 1)

# APP4-final: DP optimize APP4-draft using one dimension array, f[j]: max profit sell at j day.
# Two conditions: Fist, buy day is before j - 1, Second, buy day is on j - 1 
# f[j] = max(f[j - 1] + price[j] - price[j - 1], price[j] - price[j - 1])
# Time: O(n) Space: O(n) Runtime: 63% memory: 5%
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #     n, ans = len(prices), -sys.maxsize
    #     f = [0] * n
    #     for j in range(1, n):
    #         f[j] = max(f[j - 1] + prices[j] - prices[j - 1], prices[j] - prices[j - 1])                        
    #         ans = max(ans, f[j])
    #     # consider same day buy&sell 
    #     if ans < 0:
    #         return 0
    #     return ans 

# APP5 optimize APP2, we only need a variable instead of an array to know the lowest buy date for each sell day.
# Time: O(n) space: O(1) Runtime: 84% memory: 5%
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #     n = len(prices)
    #     lowest = sys.maxsize
    #     max_profit = -sys.maxsize
    #     for i in range(n):
    #         lowest = min(lowest, prices[i])
    #         max_profit = max(max_profit, prices[i] - lowest)
    #     if max_profit < 0:
    #         return 0
    #     return max_profit
    
# APP6: for each sell day, i only care the price smaller than its previously, so it's a increasing monotonic stack
# Time: O(n), space: O(n) Runtime: 63% memory: 5%
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        stack = []
        ans = -sys.maxsize
        # add last value to pop all the remaining ones in stack at last
        new_prices = prices + [-sys.maxsize]
        n = len(new_prices)
        for i in range(n):
            while stack and new_prices[i] < stack[-1]:
                ans = max(ans, stack[-1] - stack[0])
                stack.pop()
            stack.append(new_prices[i])
        return ans
