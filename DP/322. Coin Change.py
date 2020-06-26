class Solution:
    # APP1 Not Working: greedy, fit the largest first, but it wont work for [10, 6], 12
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        res = 0
        for coin in coins:
            res += amount // coin
            amount %= coin
            print(amount, coin, res)
        if amount:
            return -1
        return res

    # APP2: dfs, minimum count of coin starting at idx i.
    # for each coin index i(level), pick from 0 - amount // coin(for every level), then move i to another coin
    # Time: O(s ^ n), n = len(coins), s = amount // c, Space: O(1) Runtime: TLE
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        return self.dfs(coins, amount, 0)

    def dfs(self, coins, amount, idx):
        if amount == 0:
            return 0
        if idx == len(coins):
            return -1

        res, times = sys.maxsize, amount // coins[idx]
        for cnt in range(times + 1):
            left = amount - coins[idx] * cnt
            if left >= 0:
                left_cnt = self.dfs(coins, left, idx + 1)
                if left_cnt != -1:
                    res = min(res, left_cnt + cnt)
        return res if res != sys.maxsize else -1

    # APP3: dfs + memoization. each level same coin
    # Time: O(amount) space: O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        coins.sort()
        return self.dfs(coins, amount, 0, [0] * (amount + 1))

    def dfs(self, coins, amount, idx, memo):
        if amount == 0:
            return 0
        if idx == len(coins) or amount < 0:
            return -1
        if memo[amount] != 0:
            return memo[amount]
        res = sys.maxsize
        for i in range(amount // coins[idx] + 1):
            left = amount - i * coins[idx]
            left_count = self.dfs(coins, left, idx + 1, memo)
            if left_count != -1:
                res = min(res, left_count + i)
        memo[amount] = res if res != sys.maxsize else -1
        return memo[amount]

    # APP4: dfs + memoization. each level different coin
    # TIme: O(amount) space: O(amount) Runtime: 20%
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.dfs(coins, amount, {})

    def dfs(self, coins, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in memo:
            return memo[amount]
        count = sys.maxsize
        for coin in coins:
            left_count = self.dfs(coins, amount - coin, memo)
            if left_count != -1:
                count = min(count, left_count + 1)
        memo[amount] = count if count != sys.maxsize else -1
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