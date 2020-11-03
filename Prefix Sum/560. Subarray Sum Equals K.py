class Solution:
    # APP1: find all subarrays in O(n^2) and calculate each sum in O(n).
    # Time: O(n^3) space: O(1)

    # APP2: pre-process prefix sum array to know the sum in O(1)
    # Time: O(n^2) space: O(n)
    # def subarraySum(self, nums: List[int], k: int) -> int:

    # APP3: presum[i] - presum[j] = k
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or k is None:
            return 0
        now_sum, presum, res = 0, {0: 1}, 0
        for idx, num in enumerate(nums):
            now_sum += num
            if now_sum - k in presum:
                res += presum[now_sum - k]
            presum[now_sum] = presum.get(now_sum, 0) + 1
        return res
