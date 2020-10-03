class Solution:
    # APP1: brute force. Loop through array k times, every time put largest index in visited
    # Time: O(n*k) Space: O(k) Runtime: 5%
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k or k < 0:
            return None
        visited, n, res = set(), len(nums), None
        for _ in range(k):
            max_idx, max_val = -1, -sys.maxsize
            for i, val in enumerate(nums):
                if i in visited:
                    continue
                if val > max_val:
                    max_idx, max_val = i, val
            res = max_val
            visited.add(max_idx)
        return res

    #     APP2: maxheap, put all numbers in the maxheap and pop k times.
    #     Time: O(nlgn + klgn) Space: O(n) Runtime: 78%
    #     import heapq
        def findKthLargest(self, nums: List[int], k: int) -> int:
            if not nums or not k or k < 0:
                return None
            maxheap, res = [], None
            for num in nums:
                heapq.heappush(maxheap, -num)

            for _ in range(k):
                res = -heapq.heappop(maxheap)
            return res

    #     APP3: minheap, add k element to minheap, if nums[i] > minheap[0], then pop and add it, else pass.
    #     Time: O(nlgk) Space: O(k) Runtime: 78%
    #     import heapq
        def findKthLargest(self, nums: List[int], k: int) -> int:
            if not nums or not k or k < 0:
                return None

            minheap = []
            for num in nums:
                if len(minheap) < k:
                    heapq.heappush(minheap, num)
                else:
                    if num > minheap[0]:
                        heapq.heappop(minheap)
                        heapq.heappush(minheap, num)
            return minheap[0]

    #     APP4: quick select, find a pivot, move all nums that is smaller than it to it's left, all nums > pivot to it's right. check how many on the left. if count == k, return, if count > k, it must be on the left, otherwise on the right.
    #     Time: O(n) average, O(n^2) worst case Space: O(1) Runtime: 99%
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k or k < 0:
            return None
        return self.quick_select(nums, k, 0, len(nums) - 1)

    # Option1: find kth largest number between left and right.
    def quick_select(self, nums, k, start, end):
        l, r = start, end
        mid = l + (r - l) // 2
        pivot = nums[mid]
        while l <= r:
            while l <= r and nums[l] > pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if start + k - 1 <= r:
            return self.quick_select(nums, k, start, r)
        if start + k - 1 >= l:
            return self.quick_select(nums, k - (l - start), l, end)
        return nums[r + 1]

    # option2: index based, find kth largest numbers index.
    def quick_select(self, nums, k, start, end):
        if start == end:
            return nums[k - 1]
        l, r = start, end
        mid = l + (r - l) // 2
        pivot = nums[mid]
        while l <= r:
            while l <= r and nums[l] > pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if r >= k - 1:
            return self.quick_select(nums, k, start, r)
        if l <= k - 1:
            return self.quick_select(nums, k, l, end)
        return nums[r + 1]