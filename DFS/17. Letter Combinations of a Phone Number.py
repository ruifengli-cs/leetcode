class Solution:
    # APP1: build mapping info, then dfs
    # Time: O(2^n) space: O(n) stack
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        data = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        self.dfs(digits, data, 0, [], res)
        return res

    def dfs(self, digits, data, i, path, res):
        if i == len(digits):
            res.append(''.join(path))
            return
        for ch in data[digits[i]]:
            path.append(ch)
            self.dfs(digits, data, i + 1, path, res)
            path.pop()
