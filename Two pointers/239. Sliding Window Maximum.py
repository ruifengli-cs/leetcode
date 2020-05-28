import collections

class Solution:

    # use monotonic descreasing deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k is None or k < 1:
            return []
        n, ans = len(nums), []
        left = 0
        dq = collections.deque()
        for right in range(n):
            self.push(dq, nums, right)
            length = right - left + 1
            if length > k:
                if dq[0] == left:
                    dq.popleft()
                left += 1
                length -= 1
            if length == k:
                ans.append(nums[dq[0]])
        return ans

    def push(self, dq, nums, i):
        while dq and nums[i] > nums[dq[-1]]:
            dq.pop()
        dq.append(i)
