class Solution:
    #     APP1: iterate nums for starting point, then get avg value for k numbers.
    #     Time: O(nk) space: O(1)

    #     APP2: presum + sliding window.
    #     Time: O(n) space: O(1) Runtime: 62%
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return 0
        now_sum, n, left, res = 0, len(nums), 0, -sys.maxsize
        for right in range(n):
            now_sum += nums[right]
            if right - left + 1 < k:
                continue
            res = max(res, now_sum / k)
            now_sum -= nums[left]
            left += 1
        return res