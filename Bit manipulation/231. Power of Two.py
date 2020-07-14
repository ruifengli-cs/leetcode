class Solution:
    # APP1: bin() and count 1
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1

    # APP2: remove right most 1: x & (x - 1)
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0