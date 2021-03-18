# 3:39
# APP1: two pionters. loop through A for left, then extend right every time till sum == s
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        if not A or S < 0:
            return 0
        res = lsum = rsum = l = r = 0
        n = len(A)
        for i in range(n):
            l = max(i, l)
            r = max(i, r)
            while l < n and lsum + A[l] < S:
                lsum += A[l]
                l += 1
            while r < n and rsum + A[r] < S + 1:
                rsum += A[r]
                r += 1
            if l < r:
                res += r - l
            if l > i:
                lsum -= A[i]
            if r > i:
                rsum -= A[i]
        return res