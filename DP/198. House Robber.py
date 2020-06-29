class Solution:
    # APP1: DFS Time: (2^n) Space: O(1) Runtime: TLE
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.dfs(nums, 0, False)
        
    def dfs(self, nums, idx, pre_picked):
        if idx >= len(nums):
            return 0
        if pre_picked:
            res = self.dfs(nums, idx + 1, False)
        else:
            res = max(self.dfs(nums, idx + 1, True) + nums[idx], self.dfs(nums, idx + 1, False))
        return res

    # APP2: DP: f[i][0/1] max value robbing or no robbing ith house
    # f[i][0] = max(f[i - 1][1], f[i - 1][0])
    # f[i][1] = r[i] + f[i - 1][0]
    # ans = max(f[i][0], f[i][1])
    # Time: O(n) Space: O(n) Runtime: 80%
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        f = [[0] * 2 for _ in range(n)]
        f[0][0], f[0][1] = 0, nums[0]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][1], f[i - 1][0])
            f[i][1] = nums[i] + f[i - 1][0]
        return max(f[n - 1][0], f[n - 1][1])
    
#     APP3: DP: f[i]: max value robbing first ith house
#     f[i] = max(f[i - 2] + nums[i], f[i - 1])
#     f[0], f[1] = nums[0], max(nums[0], nums[1])
#     Time: O(n) space: O(n) Runtime: 94%
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        f = [0] * n
        f[0], f[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            f[i] = max(nums[i] + f[i - 2], f[i - 1])
        return f[n - 1]
