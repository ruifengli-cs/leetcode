class Solution:
# APP1: use recursion
# Time: O(2^n) Space: O(1)
# Runtime: TLE  Memory:
    def fib(self, N: int) -> int:
        if N is None or N < 0:
            return -1
        if N == 0:
            return 0
        if N == 1:
            return 1
# bug1: forget self when doing function call
        return self.fib(N - 1) + self.fib(N - 2)
        
# APP2: Recursion + memoization
# Time: O(n) Space: O(n)
# Runtime: 71%  Memory: 5%
    def fib(self, N: int) -> int:
        if N is None or N < 0:
            return -1
        memo = {0: 0, 1: 1}
        return self.dfs(N, memo)
        
    def dfs(self, N, memo):
        if N in memo:
            return memo[N]
        memo[N] = self.dfs(N - 1, memo) + self.dfs(N - 2, memo)
        return memo[N]
        
# APP3: Iteration
# Time: O(n) Space: O(1)
# Runtime: 71%  Memory: 5%
    def fib(self, N: int) -> int:
        if N is None or N < 0:
            return -1
        if N == 0:
            return 0
        if N == 1:
            return 1
        prepre, pre = 0, 1
        cur = prepre + pre
        for i in range(3, N + 1):
            prepre, pre = pre, cur
            cur = prepre + pre
        return cur
        
# APP4: DP f[i] = f[i - 1] + f[i - 2]
# Time: O(n) space: O(n)
# Runtime: 71% memory: 5%
    def fib(self, N: int) -> int:
        if N is None or N < 0:
            return -1
# bug: need to check when N == 0 what to return
        if N < 2:
            return N
        f = [0] * (N + 1)
        f[0], f[1] = 0, 1
        for i in range(2, N + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[-1]
