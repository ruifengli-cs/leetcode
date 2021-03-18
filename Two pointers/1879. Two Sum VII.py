# APP1: two pointers, pos, neg which points the largest and smallest. move just like two sum
# Time: O(n) space: O(1)
class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """

    def twoSumVII(self, nums, target):
        if not nums or target is None or len(nums) < 2:
            return []
        n, res, crossed = len(nums), set(), False
        start, is_neg_start = self.next_small(n, nums, False)
        end, is_pos_end = self.next_big(n, nums, False)
        while start < n and end < n:
            if crossed:
                break
            summ = nums[start] + nums[end]
            if summ == target:
                res.add((min(start, end), max(start, end)))
                start, is_neg_start = self.next_small(start, nums, is_neg_start)
                end, is_pos_end = self.next_big(end, nums, is_pos_end)
            elif summ > target:
                start, is_neg_start = self.next_small(start, nums, is_neg_start)
            else:
                end, is_pos_end = self.next_big(end, nums, is_pos_end)
            crossed = (is_neg_start and is_pos_end) or (is_neg_start and not is_pos_end and end <= start) or (
                        not is_neg_start and is_pos_end and end >= start)
        res = [[i, j] for i, j in res]
        return res

    def next_small(self, i, nums, is_neg_start):
        n = len(nums)
        if i == n or nums[i] > 0:
            i = i - 1
            while i >= 0 and nums[i] < 0:
                i -= 1
        if i == -1 or nums[i] <= 0:
            is_neg_start = True
            i = i + 1
            while i < n - 1 and nums[i] > 0:
                i = i + 1
        return i, is_neg_start

    def next_big(self, i, nums, is_pos_end):
        n = len(nums)
        if i == n or not is_pos_end:
            i = i - 1
            while i >= 0 and nums[i] >= 0:
                i -= 1

        if i == -1:
            is_pos_end = True
        if is_pos_end:
            i += 1
            while i < n - 1 and nums[i] < 0:
                i += 1
        return i, is_pos_end