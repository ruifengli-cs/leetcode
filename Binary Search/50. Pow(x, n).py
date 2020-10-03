class Solution:
    # APP1: recursion. Time: O(lgn) space: O(lgn) stack Runtime: 87%
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        half = self.myPow(x, n // 2)
        res = half * half
        if n & 1:
            res *= x
        return res

    # APP2: bit manipulation. Time: O(lgn) Space: O(1) Runtime:87%
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        base, res = x, 1
        while n:
            if n & 1:
                res *= base
            n >>= 1
            base = base * base
        return res