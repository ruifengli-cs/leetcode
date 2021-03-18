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


# APP3: binary search
# Time: O(m + n) space: O(1)
# To find median, we pick shortest array, binary search cut1 pos in left, right.
# n = n1 + n2. when cut1 is decided, cut2 is also decided to n // 2 - cut1
# if n is even, ans = (max(l1, l2) + min(r1, r2)) // 2
# if n is odd, ans = min(r1, r2)
# when cut is beginning or end, use minsize and maxsize as boundry.
# case1 idea: L1 < R2 and L2 < R1
# 123|4
# 3|456

# case2: L1 > R2 -> move cut1 left.
# 123|4
# 2|234

# case3: L2 > R1 -> move cut1 right.
# 1|234
# 223|4
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0

        a1, a2 = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        n1, n2 = len(a1), len(a2)
        n, half = n1 + n2, (n1 + n2) // 2
        left, right = 0, n1
        while left <= right:
            cut1 = (left + right) >> 1
            cut2 = half - cut1
            l1 = a1[cut1 - 1] if cut1 > 0 else -sys.maxsize
            r1 = a1[cut1] if cut1 < n1 else sys.maxsize
            l2 = a2[cut2 - 1] if cut2 > 0 else -sys.maxsize
            r2 = a2[cut2] if cut2 < n2 else sys.maxsize
            if l1 > r2:
                right = cut1 - 1
            elif r1 < l2:
                left = cut1 + 1
            else:
                if n & 1 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                return min(r1, r2)
