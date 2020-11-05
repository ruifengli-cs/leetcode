class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    # APP1: brute force. try from 0 to max(L)
    # Time: O(max(L)*len(L)) space: O(1)

    # APP2: binary search answer
    # Time: O(lg(max(L)*len(L))) space:O(1)
    def woodCut(self, L, k):
        if not L or not k:
            return 0
        start, end = 1, max(L)
        while start + 1 < end:
            mid = (start + end) >> 1
            if self.has_solution(mid, k, L):
                start = mid
            else:
                end = mid
        if self.has_solution(end, k, L):
            return end
        if self.has_solution(start, k, L):
            return start
        return 0

    def has_solution(self, mid, k, L):
        res = 0
        for wood in L:
            res += wood // mid
        return res >= k
