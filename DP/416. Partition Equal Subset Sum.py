class Solution:
    # APP1: DFS, try all comb for subset1 and calculate. 
    # Time: O(2^n) space: O(1) stack space: O(n) Runtime: TLE
        def canPartition(self, nums: List[int]) -> bool:
            if not nums:
                return True
            return self.dfs(nums, 0, 0, sum(nums) / 2)

        def dfs(self, nums, i, summ, half):
            if summ == half:
                return True
            if summ > half or i >= len(nums):
                return False
            if self.dfs(nums, i + 1, summ, half) or self.dfs(nums, i + 1, summ + nums[i], half):
                return True
            return False

    # APP2 not working: sort. two pointers opposite directions. start with right, then left.
    # Time: O(nlgn) space: O(n)
        def canPartition(self, nums: List[int]) -> bool:
            if not nums:
                return True
            half, l, r, cur_sum = sum(nums) / 2, 0, len(nums) - 1, 0
            nums.sort()
            print(nums, half)
            while cur_sum <= half:
                if cur_sum == half:
                    return True
                if cur_sum + nums[r] <= half:
                    cur_sum += nums[r]
                    r -= 1
                else:
                    cur_sum += nums[l]
                    l += 1
            return False

    # APP3: memoization based on dfs. memo[(i, sum)]
    # Time: O(n^2) space: O(n^2) Runtime: 5%
        def canPartition(self, nums: List[int]) -> bool:
            if not nums:
                return True
            memo, half = {}, sum(nums) / 2
            return self.dfs(nums, 0, 0, half, memo)

        def dfs(self, nums, i, summ, half, memo):
            if summ == half:
                return True
            if summ > half or i >= len(nums):
                return False
            if (i, summ) in memo:
                return memo[(i, summ)]
            memo[(i, summ)] = False
            if self.dfs(nums, i + 1, summ, half, memo) or self.dfs(nums, i + 1, summ + nums[i], half, memo):
                memo[(i, summ)] = True
            return memo[(i, summ)]

    # APP4: dp[i][j]: if first i num can form sum j. ans: dp[n - 1][half]
    # dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]], dp[0][0] = True
    # optimize using 1d array. 
    # new[j] = old[j] or old[j - nums[i]]
    # Time; O(n*half) space: O(half) runtime: 50%
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        total = sum(nums)
        if total % 2:
            return False
        n, half = len(nums), total // 2
        new, old = [False] * (half + 1), [True] + [False] * (half)
        for i in range(n):
            for j in range(half + 1):
                new[j] = old[j]
                if j - nums[i] >= 0:
                    new[j] |= old[j - nums[i]]
                if j == half and new[j]:
                    return True
            new, old = old, new
        return False