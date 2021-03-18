class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        if not encoded:
            return []
        res = [first]
        for i in encoded:
            first = first ^ i
            res.append(first)
        return res

# input: 1,0,2,1

# encod: 1,2,3
# arr = [1,0]
# 11
# 10
# 10 xor c = 11

# 01

# 0 xor c xorc = 10 xor c
# 0 xor c xor c = 0

# 0 xor c = 10
# 10 xor c = 0