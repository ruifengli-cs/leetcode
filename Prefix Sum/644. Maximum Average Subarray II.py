class Solution:
    #     APP1: iterate through nums for start, get all comb avg value then find the max.
    #     Time: O(n^2) space: O(1)

    #     APP2: binary search answer to guess what solution maybe, then see if there's a valid solution.
    #     Time: O(lg(max-min)n) space: O(n)
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or not k:
            return 0
        start, end = min(nums), max(nums)
        while end - start > 1e-5:
            mid = (end + start) / 2
            if self.has_solution(nums, k, mid):
                start = mid
            else:
                end = mid
        return start

    def has_solution(self, nums, k, avg):
        presum, n, min_presum = [0], len(nums), 0
        # use every num - avg and then get presum
        for i in range(n):
            presum.append(presum[-1] + nums[i] - avg)

        for i in range(k, n + 1):
            if presum[i] - min_presum >= 0:
                return True
            min_presum = min(min_presum, presum[i - k + 1])

        return False