# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


# Solution1: brute force, loop through list k times and each time find largest then exclude it.
# Time: O(n^2) space: O(k)

# Solution2: sort the list in descending order, then loop through list and find kth largest
# Time: O(nlgn) space: O(1)

# Solution3: maxheap, loop through list then put every num in maxheap, then pop k times
# Time: O(n) space: O(n)

# Solution4: quick select. find a pivot, then partition the list based on the pivot.
# partition logic: move everything that is => pivot to the right
# left, right
# if len(right) > k, then the res is in the right part,
# if len(right) == k, then pivot is the res
# else res is in the left part
# Time: O(n) space: O(1)
#     [3,2,3,1,2,4,5,5,6] O(n)
#     pivot = 2
#     [1,3,2,3,2,4,5,5,6] O(n/2)
#     pivot
#     n + n/2 + n/4 .. + 1 = O(n)

# quick select
# partition: return how many number on right, move the nums

https: // leetcode.com / problems / kth - largest - element - in -an - array /


class Solution:
    def findKthLargest(self, nums, k) -> int:
        if not nums or not k or k < 0:
            return -1

        return self.partition(nums, 0, len(nums) - 1, len(nums) - k)

    def partition(self, nums, start, end, k):
        if start == end:
            return nums[k]

        pivot = nums[start + (end - start) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if left <= k:
            return self.partition(nums, left, end, k)
        else:
            return self.partition(nums, start, right, k)


# import heapq
# class Solution:
#     def findKthLargest(self, nums, k) -> int:
#         if not nums or not k or k < 0:
#             return -1
#         maxheap = []
#         for num in nums:
#             heapq.heappush(maxheap, -num)
#         for _ in range(k):
#             res = -heapq.heappop(maxheap)
#         return res

sol = Solution()
input1 = [3, 2, 1, 5, 6, 4]
input2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(sol.findKthLargest(input2, 4))