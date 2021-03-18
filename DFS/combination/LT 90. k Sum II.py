import copy


class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        if not A or k < 0:
            return []
        res = []
        self.dfs(A, k, target, 0, [], res)
        return res

    def dfs(self, nums, k, target, idx, path, res):
        if target == 0 and k == 0:
            res.append(copy.deepcopy(path))
            return
        if target < 0 or k < 0 or idx == len(nums):
            return
        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.dfs(nums, k - 1, target - nums[i], i + 1, path, res)
            path.pop()