class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """

    # APP1: brute force find all subarraysand calculate each sum
    # Time: O(n^2) space: O(1) Runtime: TLE
    def subarraySumEqualsKII(self, nums, k):
        if not nums or k is None:
            return -1
        n = len(nums)
        min_len = sys.maxsize
        for i in range(n):
            now_sum = 0
            for j in range(i, n):
                now_sum += nums[j]
                if now_sum == k:
                    min_len = min(min_len, j - i + 1)
        if min_len == sys.maxsize:
            return -1
        return min_len

    # APP2: brute force2: pre-process prefix sum array to know the sum in O(1)
    # Time: O(n^2) space: O(n), Runtime: TLE
    def subarraySumEqualsKII(self, nums, k):
        if not nums or k is None:
            return -1
        now_sum = 0
        n = len(nums)
        prefix_sum = [0]
        min_len = sys.maxsize
        for num in nums:
            now_sum += num
            prefix_sum.append(now_sum)
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                # pruning
                if j - i + 1 > min_len:
                    break
                if prefix_sum[j] - prefix_sum[i - 1] == k:
                    min_len = min(min_len, j - i + 1)
        return min_len if min_len != sys.maxsize else -1

    # APP3: from presum array, we need presum[j] - presum[i] = key, like two sum, we can use hashmap[presum[i]: i]
    # Time: O(n) space: 2*O(n), two pass.
    def subarraySumEqualsKII(self, nums, k):
        if not nums:
            return -1
        now_sum = 0
        n = len(nums)
        presum = []
        mapping = {0: -1}
        ans = sys.maxsize
        for num in nums:
            now_sum += num
            presum.append(now_sum)
        for i in range(n):
            if presum[i] - k in mapping:
                ans = min(ans, i - mapping[presum[i] - k])
            else:
                mapping[presum[i]] = i
        return ans if ans != sys.maxsize else -1
