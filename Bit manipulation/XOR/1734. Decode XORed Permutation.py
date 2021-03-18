# APP1: need to find the first element in origin,
# origin[i] ^ origin[i + 1] = ecoded[i] => origin[i + 1] = ecoded[i] ^ origin[i]
# how to find origin[0]?
# 1. we can get XOR of total n permutaion.
# 2. then since origin is odd, we can get pair without head.
# 3. use step 1, 2 to get head
# Time: O(n) space: O(n) Runtime: 50%
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total ^= i
        nohead = 0
        for i in range(1, n - 1, 2):
            nohead ^= encoded[i]
        head = total ^ nohead
        res = [head]
        for i in range(n - 1):
            res.append(res[-1] ^ encoded[i])
        return res