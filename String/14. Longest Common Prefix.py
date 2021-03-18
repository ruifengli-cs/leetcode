class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        original = strs[0]
        for i in range(1, len(strs)):
            j, n = 0, len(original)
            while j < n and j < len(strs[i]):
                if original[j] != strs[i][j]:
                    break
                j += 1
            if j < n:
                original = original[:j]
        return original
