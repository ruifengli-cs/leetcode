class Solution:
    # APP1: like fibonicci sequence. use recursion(dfs)
    # Time: O(2^n) Space: O(1) Runtime: TLE
    # def climbStairs(self, n: int) -> int:
    #     if not n or n < 0:
    #         return 0
    #     if n <= 2:
    #         return n
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # APP2: optimize APP1: dfs + memoization
    # Time: O(n) space: O(n) Runtime: 71% memory: 6%
    #     def climbStairs(self, n: int) -> int:
    #         if not n or n < 0:
    #             return 0
    #         if n <= 2:
    #             return n
    #         memo = {1: 1, 2: 2}
    #         return self.dfs(n, memo)

    #     def dfs(self, n, memo):
    #         if n in memo:
    #             return memo[n]
    #         memo[n] = self.dfs(n - 1, memo) + self.dfs(n - 2, memo)
    #         return memo[n]

    # APP3: DP. Define f[i]: distinct ways to reach ith stairs.
    # f[i] = f[i - 1] + f[i - 2]. ans = f[n - 1]
    # Time: O(n) Space: O(n) Runtime: 98% memory:6%
    #     def climbStairs(self, n: int) -> int:
    #         if not n or n < 0:
    #             return 0
    #         if n <= 2:
    #             return n
    #         f = [1, 2] + [0] * (n - 2)
    #         for i in range(2, n):
    #             f[i] = f[i -1] + f[i - 2]
    #         return f[n - 1]

    # APP4: optimize APP3. we only need to know the state of i - 1 and i - 2. Two variables will do
    # Time: O(n) Space: O(1) Runtime: 98% Memory:6%
    def climbStairs(self, n: int) -> int:
        if not n or n < 0:
            return 0
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(2, n):
            c = a + b
            a, b = b, c
        return c
