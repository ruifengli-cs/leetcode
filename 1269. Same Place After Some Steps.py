class Solution:
# APP1: dfs. Time: O(3^n), n = steps Space: O(1) Runtime: TLE
    def numWays(self, steps: int, arrLen: int) -> int:
        if not steps or steps < 0 or not arrLen or arrLen < 0:
            return -1
        return self.dfs(steps, arrLen, 0) % 10 ** 9 + 7
    
    def dfs(self, steps, arrLen, cur_index):
        if cur_index < 0 or cur_index >= arrLen:
            return 0
        if steps == 0:
            if cur_index == 0:
                return 1
            else:
                return 0
        return self.dfs(steps - 1, arrLen, cur_index - 1) +  self.dfs(steps - 1, arrLen, cur_index) +  self.dfs(steps - 1, arrLen, cur_index + 1)
    
# APP2: dfs + memoization. Time: O(steps * min(arrLen, steps + 1)), space: O(steps * min(arrLen, steps + 1))
# Runtime:
    def numWays(self, steps: int, arrLen: int) -> int:
        if not steps or steps < 0 or not arrLen or arrLen < 0:
            return 0
        memo = {}
        return self.dfs(steps, arrLen, 0, memo)
    
#     def dfs(self, steps, arrLen, pos, memo):
#         if (steps, pos) in memo:
#             return memo[(steps, pos)]
#         if pos < 0 or pos > arrLen - 1:
#             return 0
#         if steps == 0:
#             return 1 if pos == 0 else 0
#         memo[(steps, pos)] = self.dfs(steps - 1, arrLen, pos - 1, memo) \
#         + self.dfs(steps - 1, arrLen, pos, memo) + self.dfs(steps - 1, arrLen, pos + 1, memo)
#         return memo[(steps, pos)] % (10 ** 9 + 7)

        # if not steps or not arrLen or steps < 0 or arrLen < 0:
        #     return 0
        # memo = {}
        # self.dfs(steps, arrLen, 0, memo)
        # return memo[(0, 0)]
        
    def dfs(self, steps, arrLen, cur_index, memo):
        if (steps, cur_index) in memo:
            return memo[(steps, cur_index)]
        if cur_index < 0 or cur_index >= arrLen:
            return 0
        if steps == 0:
            return 1 if cur_index == 0 else 0
        memo[(steps, cur_index)] = (self.dfs(steps - 1, arrLen, cur_index - 1, memo) + self.dfs(steps - 1, arrLen, cur_index, memo) + self.dfs(steps - 1, arrLen, cur_index + 1, memo) ) % (10 ** 9 + 7)
        return memo[(steps, cur_index)] 
        
# APP3: DP: f[i][j]: numb of ways at step i, index j. Two demention array + optimize arrLen
# f[i][j] = f[i - 1][j - 1] + f[i - 1][j] + f[i - 1][j + 1]
# Time: O(steps * min(arrlen, steps + 1)) Space: O(steps * min(arrlen, steps + 1)) Runtime: 20%
    def numWays(self, steps: int, arrLen: int) -> int:
        if not steps or not arrLen or steps < 0 or arrLen < 0:
            return -1
        arrLen = min(arrLen, steps + 1)
        f = [[0] * arrLen for _ in range(steps + 1)]
        f[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(arrLen):
                f[i][j] += f[i - 1][j]
                if j > 0:
                    f[i][j] += f[i - 1][j - 1]
                if j < arrLen - 1:
                    f[i][j] += f[i - 1][j + 1]
        return f[steps][0] % (10 ** 9 + 7)
    
# APP3: DP: f[i][j]: numb of ways at step i, index j. Optimize APP4 using rolling array
# Time: O(steps * min(arrlen, steps + 1)) Space: O(min(arrlen, steps + 1))
    def numWays(self, steps: int, arrLen: int) -> int:
        if not steps or not arrLen or steps < 0 or arrLen < 0:
            return -1
        arrLen = min(arrLen, steps + 1)
        pre = [1] + [0] * (arrLen - 1)
        cur = [0] * arrLen
        for _ in range(steps):
            for i in range(arrLen):
                cur[i] = 0
                cur[i] += pre[i]
                if i > 0:
                    cur[i] += pre[i - 1]
                if i < arrLen - 1:
                    cur[i] += pre[i + 1]
            pre, cur = cur, pre
        return pre[0] % (10 ** 9 + 7)
