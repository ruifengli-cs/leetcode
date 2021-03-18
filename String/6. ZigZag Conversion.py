# APP1; iterate input, put char in res lists.
# Time: O(n) space: O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows <= 1:
            return s
        res = [[] for _ in range(numRows)]
        res[0].append(s[0])
        row, flag = 1, 1
        for ch in s[1:]:
            res[row].append(ch)
            if row == numRows - 1 or row == 0:
                flag = -flag
            row += flag
        final = []
        for new_row in res:
            final += new_row
        return "".join(final)