class Solution:
    # APP1: for loop of 32.
    # Time: O(1) Space: O(1) Runtime: 50%
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n = n >> 1
        return res

    # APP2: reverse to the correct pos directly
    # Time: O(1) space: O(1) Runtime: 80%
    def reverseBits(self, n: int) -> int:
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
        return res