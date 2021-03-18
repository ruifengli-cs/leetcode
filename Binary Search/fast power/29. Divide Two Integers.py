# APP1: assume x / y = 9, 9 can be represented in binary 1 + 8 = 1001
# pre-calculate y * k: 1y, 2y, 4y,8y
# loop from big to small for k*k, use x minus it
# Time: O(lgk) space: O(lgk) Runtime: 70%
class Solution:
    def divide(self, x: int, y: int) -> int:
        if y == 0:
            return 2 * 31 - 1
        # check is_neg
        sign = -1 if (x < 0 and y > 0 or (x > 0 and y < 0)) else 1
        a, b = abs(x), abs(y)

        # pre-calculate
        exp, base = [], b
        while base <= a:
            exp.append(base)
            base += base

        # get result
        res = 0
        for i in range(len(exp) - 1, -1, -1):
            if a >= exp[i]:
                res += 1 << i
                a -= exp[i]

        # check res is out bound or neg
        res *= sign
        if res > 2 ** 31 - 1 or res < - 2 ** 31:
            return 2 ** 31 - 1
        return res