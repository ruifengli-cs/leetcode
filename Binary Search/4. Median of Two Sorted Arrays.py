class Solution:
    #     APP1: brute force, merge two sorted list then find median.
    #     Time: O(m + n) Space: O(m + n)

    #     APP2: binary search answer
    #     Time: O(lg(range) * (lgn + lgm)) Space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        size = m + n
        if not nums1:
            return (nums2[size // 2] + nums2[(size - 1) // 2]) / 2
        if not nums2:
            return (nums1[size // 2] + nums1[(size - 1) // 2]) / 2
        start, end = min(nums1[0], nums2[0]), max(nums1[-1], nums2[-1])
        if size % 2 == 0:
            small = self.find_kth(nums1, nums2, start, end, size // 2)
            big = self.find_kth(nums1, nums2, start, end, size // 2 + 1)
            return (small + big) / 2
        return self.find_kth(nums1, nums2, start, end, size // 2 + 1)

    def find_kth(self, nums1, nums2, start, end, k):
        while start < end:
            mid = (start + end) >> 1
            count = self.find_eq_less(nums1, nums2, mid)
            if count >= k:
                end = mid
            else:
                start = mid + 1
        return start

    def find_eq_less(self, nums1, nums2, target):
        import bisect
        cnt1 = bisect.bisect_right(nums1, target)
        cnt2 = bisect.bisect_right(nums2, target)
        return cnt1 + cnt2

    #     APP3: binary search.
    #     https://blog.csdn.net/chen_xinjia/article/details/69258706
    #     1. find smaller array, use binary search to cut.
    #     2. ideally we should have L1 | R1, L2 | R2 and L2 = size // 2 - L1 and L1 < R2 and L2 < R1
    #     3. if L1 > R2, cutR = cut1 - 1, if L2 > R1, curL = cut1 + 1. else return
    #     4. you might cut at 0 or at end, treat it as -sys.maxsize and sys.maxisize
    #     Time: O(lg(min(m, n))), space: O(1) Runtime: 90%
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_s, nums_l = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        m, n = len(nums_s), len(nums_l)
        size = m + n
        if not nums_s:
            return (nums_l[size // 2] + nums_l[(size - 1) // 2]) / 2
        left, right = 0, m
        while left <= right:
            cut1 = (left + right) >> 1
            cut2 = size // 2 - cut1
            val1_l = nums_s[cut1 - 1] if cut1 > 0 else -sys.maxsize
            val1_r = nums_s[cut1] if cut1 < m else sys.maxsize
            val2_l = nums_l[cut2 - 1] if cut2 > 0 else -sys.maxsize
            val2_r = nums_l[cut2] if cut2 < n else sys.maxsize
            if val1_l > val2_r:
                right = cut1 - 1
            elif val2_l > val1_r:
                left = cut1 + 1
            else:
                if size % 2 == 0:
                    return (max(val1_l, val2_l) + min(val1_r, val2_r)) / 2
                return min(val1_r, val2_r)
        return -1
