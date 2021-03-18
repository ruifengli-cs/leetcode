class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """

    # APP1: brute force. get presum then use two pointers to get the count
    # Time: O(n^2) space: O(n)
    # def subarraySumII(self, A, start, end):
    #     if not A or end < start:
    #         return 0
    #     n, res, presum, nowsum = len(A), 0, [0], 0
    #     # get presum
    #     for num in A:
    #         nowsum += num
    #         presum.append(nowsum)

    #     for i in range(n + 1):
    #         j = i + 1
    #         while j < len(presum) and presum[j] - presum[i] <= end:
    #             if presum[j] - presum[i] >= start:
    #                 res += 1
    #             j += 1
    #     return res

    # APP2: 3 pointers. left, r_start, r_end. [left, r_start]is the left bountry for left. vice versa.
    # 1,2,3,4         1-3     [1], [1,2], [2], [3]
    # 0,1,3,6,10
    #   i
    #   l
    #   r
    # res = 2
    def subarraySumII(self, A, start, end):
        if not A or end < start:
            return 0
        n, res, nowsum, left, presum = len(A), 0, 0, 0, [0]
        # get presum
        for num in A:
            nowsum += num
            presum.append(nowsum)

        r_start = r_end = 1
        for i in range(n + 1):
            r_start = max(i + 1, r_start)
            while r_start <= n and presum[r_start] - presum[i] < start:
                r_start += 1
            r_end = max(r_end, r_start)
            while r_end <= n and presum[r_end] - presum[i] <= end:
                r_end += 1
            if r_end > r_start:
                res += r_end - r_start
        return res

# 3 pointers
# APP1: 3pointers
# Time: O(n) space: O(1)
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, nums, start, end):
        if not nums:
            return 0
        left = right = left_sum = right_sum = res = 0
        n = len(nums)
        for i in range(n):
            left = max(left, i)
            right = max(right, i)
            while left < n and left_sum + nums[left] < start:
                left_sum += nums[left]
                left += 1
            while right < n and right_sum + nums[right] <= end:
                right_sum += nums[right]
                right += 1
            if left < right:
                res += right - left
            if left > i:
                left_sum -= nums[i]
            if right > i:
                right_sum -= nums[i]
        return res