class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsKII(self, nums, k):
        if not nums or not k or k < 0:
            return -1
        mapping, n = {0: -1}, len(nums)
        now_sum, min_len = 0, n + 1
        for i in range(n):
            now_sum += nums[i]
            need = now_sum - k
            if need in mapping:
                min_len = min(min_len, i - mapping[need])
            mapping[now_sum] = i
        if min_len == n + 1:
            return -1
        return min_len