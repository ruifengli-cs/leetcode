class Solution:
    #     Attepmt 1 - NOT WORKING: loop through list for starting point, then find its increasing subsequence
    # it won't work because eg [1,100,2,3,4]
    #     Time: O(n^2) space: O(1)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n, res = len(nums), 1
        for i in range(n - 1):
            cur, LIS = nums[i], 1
            for j in range(i + 1, n):
                if nums[j] > cur:
                    LIS += 1
                    cur = nums[j]
            res = max(res, LIS)
        return res

    #     Attempt 2 - NOT WORKING: increasing monotonic stack
    # it won't work because eg [1,100,2,3,4]
    #     Time: O(n) space: O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        stack, res = [], 0
        for num in nums:
            while stack and num <= stack[-1]:
                stack.pop()
            stack.append(num)
            res = max(res, len(stack))
        return res

    # APP1: brute force dfs with global variable. for each pos, we can pick or not pick. only pick larger one
    # Time: O(2^n) space: O(n) stack Runtime: TLE
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.res = 0
        self.dfs(nums, 0, -sys.maxsize, 0)
        return self.res

    def dfs(self, nums, i, pre, cur_len):
        if i == len(nums):
            self.res = max(self.res, cur_len)
            return
        self.dfs(nums, i + 1, pre, cur_len)
        if nums[i] > pre:
            self.dfs(nums, i + 1, nums[i], cur_len + 1)

    # APP2: brute force dfs without global variable. cleaner way for opimization later.
    # Time: O(2^n) space: O(n) stack Runtime: TLE
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.dfs(nums, 0, -sys.maxsize)

    def dfs(self, nums, i, pre):
        if i == len(nums):
            return 0
        res = self.dfs(nums, i + 1, pre)
        if nums[i] > pre:
            res = max(res, 1 + self.dfs(nums, i + 1, nums[i]))
        return res

    # APP3: dfs + memoization.
    # Time: O(n^2) space: O(n^2) runtime: 5%
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = {}
        return self.dfs(nums, memo, 0, -sys.maxsize)

    def dfs(self, nums, memo, i, pre):
        if i == len(nums):
            return 0
        if (i, pre) in memo:
            return memo[(i, pre)]
        res = self.dfs(nums, memo, i + 1, pre)
        if nums[i] > pre:
            res = max(res, 1 + self.dfs(nums, memo, i + 1, nums[i]))
        memo[(i, pre)] = res
        return res

    # APP4: DP. f[i]: LIS upto index i, including nums[i], ans = max(f)
    # f[i] = 1 + max(f[j]) where 0 <= j < i, find max f[j] when nums[j] < nums[i]
    # Time: O(n^2) space: O(N^2) Runtime: 66%
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        f = [0] * n
        for i in range(n):
            length, max_lis = 1, 0
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    max_lis = max(max_lis, f[j])
            f[i] = max_lis + 1
        return max(f)

    # APP5: DP + binary search. f[i]: last min num for LIS at length i.
    # artical: https://bit.ly/33Z7Y4C
    # Time: O(nlgn) space: O(n) Runtime: 99.8%
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = []
        for i in range(len(nums)):
            if not f or nums[i] > f[-1]:
                f.append(nums[i])
            else:
                pos = bisect.bisect_left(f, nums[i])
                f[pos] = nums[i]
        return len(f)
