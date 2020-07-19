class Solution:
    # APP1: use bin() and str.count('1')
    # Time: O(num * k) space: O(1) Runtime: 44%
    def countBits(self, num: int) -> List[int]:
        if not num or num < 0:
            return [0]
        res = []
        for i in range(num + 1):
            res.append(bin(i).count('1'))
        return res

    # APP2: use n & (n - 1) to count 1
    # Time: O(num * k) space: O(1) Runtime: 16%
    def countBits(self, num: int) -> List[int]:
        if not num or num < 0:
            return [0]
        res = []
        for i in range(num + 1):
            res.append(self.get_count(i))
        return res

    def get_count(self, n):
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count

    # APP3: DP f[i]: count of the 1's for i
    # f[i] = f[i >> 1] + (i & 1)
    # TIme: O(num) space: O(1) Runtime: 18%
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res
