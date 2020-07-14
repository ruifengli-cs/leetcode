class Solution:
    # APP1: for loop and check last digit is 1, then shift right n.
    # Time: O(lgn) space: O(1)
    def hammingWeight(self, n: int) -> int:
        print(n)
        if not n:
            return 0
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count

    # APP2: remove right most 1 x = x & (x - 1)
    # Time: O(num of 1s) space: O(1)
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count

    # APP3: use bin() and str.count()
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')