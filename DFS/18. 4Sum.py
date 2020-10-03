class Solution:
    # APP1: DFS get ksum. if k == 2 then get 2sum.
    # Time: upperbound: O(n^(k - 1)) space: O(n)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        print(nums)
        return self.dfs(nums, target, 0, 4)

    def dfs(self, nums, t, idx, k):
        if idx >= len(nums) or len(nums) - idx < k or nums[idx] * k > t or nums[-1] * k < t:
            return []
        if k == 2:
            return self.two_sum(nums, t, idx)
        res = []
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            for comb in self.dfs(nums, t - nums[i], i + 1, k - 1):
                res.append([nums[i]] + comb)
        return res

    # can't use hashmap for two sum
    # def two_sum(self, nums, t, idx):
    #     mapping, res = {}, []
    #     for i in range(idx, len(nums)):
    #         if t - nums[i] in mapping:
    #             res.append([t - nums[i], nums[i]])
    #         mapping[nums[i]] = i
    #     return res

    def two_sum(self, nums, target, start):
        res, n = [], len(nums)
        l, r = start, n - 1
        # print(nums[l], nums[r], target, start)
        while l < r:
            now_sum = nums[l] + nums[r]
            if now_sum < target or (l > start and nums[l] == nums[l - 1]):
                l += 1
            elif now_sum > target or (r < n - 1 and nums[r] == nums[r + 1]):
                r -= 1
            else:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
        return res