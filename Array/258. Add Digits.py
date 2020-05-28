class Solution:
    # APP1: recursion. add all digits, if resul // 10 >= 1, do it recursionly.
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        if num // 10 < 1:
            return num
        res = 0
        while num:
            res += num % 10
            num //= 10
        return self.addDigits(res)

    # APP2: as N = a[0] * 1 + a[1] * 10 + a[2] * 100 + ....a[n] * 10^n, M = a[0] + a[1] + a[2] +..+a[n]
    # also as 1 % 9 = 1, 10 % 9 = 1, then we know N % 9 = M, thus M = N % 9
    # since 9 % 9 = 0, so we make M = (N - 1) % 9 + 1
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        return (num - 1) % 9 + 1