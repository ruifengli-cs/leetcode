class Solution:
# APP1: dfs: fewest number of coins that you need to make up that amount
# for each coin, you can pick it for amount // coin[i] times
# Time: O(s^n) where n = len(coins), s = amount / coin[i]
# space: O(1). Runtime: TLE

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or not amount:
            return 0
        return self.dfs(coins, 0, amount, len(coins))

    def dfs(self, coins, idx, amount, n):
        if amount == 0:
            return 0
        if idx == n:
            return -1
        res = sys.maxsize
        for i in range(amount // coins[idx] + 1):
            left = amount - coins[idx] * i
            left_cnt = self.dfs(coins, idx + 1, left, n)
            if left_cnt != -1:
                res = min(res, i + left_cnt)
        return res if res != sys.maxsize else -1

# APP2: dfs + memoization. Optimize APP1
# Time: O(amount * n) space: O(amount * n) Runtime: TLE
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or not amount:
            return 0
        return self.dfs(coins, amount, 0, len(coins), {})

    def dfs(self, coins, amount, idx, n, memo):
        if amount == 0:
            return 0
        if idx == n:
            return -1
        if (amount, idx) in memo:
            return memo[(amount, idx)]
        res = sys.maxsize
        for i in range(amount // coins[idx] + 1):
            left = amount - coins[idx] * i
            left_cnt = self.dfs(coins, left, idx + 1, n, memo)
            if left_cnt != -1:
                res = min(res, i + left_cnt)
        memo[(amount, idx)] = res if res != sys.maxsize else -1
        return memo[(amount, idx)]

# APP3: dfs: fewest number of coins that you need to make up that amount
# each time, pick any coin from coins
# Time: (s^n) space: O(1) RUntime: Tle
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or not amount:
            return 0
        return self.dfs(coins, amount)

    def dfs(self, coins, amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        num = sys.maxsize
        for coin in coins:
            cnt = self.dfs(coins, amount - coin)
            if cnt != -1:
                num = min(num, cnt)
        return num + 1 if num != sys.maxsize else -1

# APP4: dfs + memoization. Optimize APP3
# Time: O(amount) space: O(amount) Runtime: 34%
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or not amount:
            return 0
        return self.dfs(coins, amount, {})

    def dfs(self, coins, amount, memo):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        num = sys.maxsize
        for coin in coins:
            cnt = self.dfs(coins, amount - coin, memo)
            if cnt != -1:
                num = min(num, cnt)
        memo[amount] = num + 1 if num != sys.maxsize else -1
        return memo[amount]

    #     APP5: bottom up DP. f: fewest number of coins that you need to make up i amount. ans: f[amount]
    #     f[i] = min(f[i - c1], f[i - c2], f[i - c3]) + 1
    #     f[0] = 0
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or not amount:
            return 0
        n = len(coins)
        f = [sys.maxsize] * (amount + 1)
        f[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                f[i] = min(f[i], f[i - coin] + 1)
        return f[amount] if f[amount] != sys.maxsize else -1