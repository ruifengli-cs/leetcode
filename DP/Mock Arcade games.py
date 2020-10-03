# Adam is so good at playing arcade games that he will win at every game he plays.
# One fine day as he was walking on the street,
# he discovers an arcade store that pays real cash for every game that the player wins -
# however, the store will only pay out once per game.
# The store has some games for which they will pay winners,
# and each game has its own completion time and payout rate.
# Thrilled at the prospect of earning money for his talent,
# Adam walked into the store only to realize that the store closes in 2 hours (exactly 120 minutes).
# Knowing that he cannot play all the games in that time,
# he decides to pick the games that maximize his earning.

# Inputs:

# games = ["Pac-man", "Mortal Kombat", "Super Tetris", "Pump it UP", "Street Fighter II", "Speed Racer"]

# completion_time = [90, 10, 25, 10, 90, 10] (in minutes)

# payout_rate = [400, 30, 100, 40, 450, 40]

# Question:

# Write code to help Adam pick the sequence of games that earn him the most money.

# Then, assume you have a variable list of games and their payout rates.
# What is the best way to pick the games that earn you the most?

# Output:

# output the game names that earn him the most into the standard output in alphabetical order.

# output = ["Mortal Kombat", "Pump it Up", "Speed Racer", "Street Fighter II"]

# 10 + 10 + 10 + 90
# 30 + 40 + 40 + 450

# 120
# step1:
# for each game, I can pick or not pick it.
# dp[i][j]: for first ith games, when total completion time is j, how much rate he can get
# dp[0][...] = 0
# dp[...][0] = 0
# dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - c_time[i]] + rate[i]))

# during step1:
# array = [0, 1, 0, 1], len(array) == len(games)
# if pick, then mark cur as 1 else 0

# step2:
# sort the res

# Time: O(n * 120 + mlgm) space: O(n * 120)
# dp
# row: 0 - n - 1
# col: 0 - 120
import collections
class Solution:
    def max_rate(self, games, time, rates):
        if not games or not time or not rates:
            return 0
        res, n = [], len(games)
        dp, select = [[0] * 121 for _ in range(n + 1)], collections.defaultdict(list)
        for i in range(1, n + 1):
            for j in range(121):
                val_p = dp[i - 1][j - time[i - 1]] + rates[i - 1] if j - time[i - 1] >= 0 else 0
                val_np = dp[i - 1][j]
                if val_p > val_np:
                    dp[i][j] = val_p
                    select[(i, j)] = select.get((i - 1, j - time[i - 1]), []) + [1]
                else:
                    dp[i][j] = val_np
                    select[(i, j)] = select.get((i - 1, j), []) + [0]
        selected_games = select[(n, 120)]
        for i in range(n):
            if selected_games[i]:
                res.append(games[i])
        res.sort()
        return res


sol = Solution()
games = ["Pac-man", "Mortal Kombat", "Super Tetris", "Pump it UP", "Street Fighter II", "Speed Racer"]
time = [90, 10, 25, 10, 90, 10]
rates = [400, 30, 100, 40, 450, 40]
print(sol.max_rate(games, time, rates))


import collections
import sys


class Solution:
    """
    @input: names -> list of game names (string)
            times -> list of time (int) the game will cost
            moneys -> list of money (int) he could get
    @output: int -> max money he could get
    @print: print the best plan for him
    """

    def get_most_money_for_game(self, names, times, moneys):
        if not names:
            return 0
        dp = [-1] * 121
        dp[0] = 0
        L = len(names)

        pi = [[False] * 121 for i in range(L)]  # path indicator

        for i in range(L):
            for t in range(120, -1, -1):
                if t - times[i] < 0 or dp[t - times[i]] < 0:
                    continue
                dp[t] = max(dp[t - times[i]] + moneys[i], dp[t])

                if dp[t] == dp[t - times[i]] + moneys[i]:
                    pi[i][t] = True

        last_time = 0
        game_list = []
        idx = L - 1
        res = 0
        for t in range(121):
            res = max(res, dp[t])
            if res == dp[t]:
                last_time = t

        while last_time > 0:
            while idx >= 0 and not pi[idx][last_time]:
                idx -= 1
            game_list.append(names[idx])
            last_time -= times[idx]
            idx -= 1

        game_list.sort()
        for name in game_list:
            print(name)

        return res


if __name__ == "__main__":

    print("please input the game info below:")

    names, times, moneys = [], [], []
    cases = int(sys.stdin.readline().strip())

    while cases > 0:
        line = sys.stdin.readline().strip()
        item = line.split(",")
        names.append(item[0])
        times.append(int(item[1]))
        moneys.append(int(item[2]))

        cases -= 1

    S = Solution()
    print("The best plan for him is:")
    res = S.get_most_money_for_game(names, times, moneys)
    print("Max money he could get is: " + str(res))

