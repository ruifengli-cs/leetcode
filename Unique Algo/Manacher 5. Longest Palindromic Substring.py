class Solution:
    # APP1: find all the substrings and check palindrom, find the longest.
    # Time: O(n^3) Space: O(1) Runtime: TLE
    #     def longestPalindrome(self, s: str) -> str:
    #         if not s:
    #             return s
    #         n, lps = len(s), (0, 0, 0)
    #         for i in range(n - 1):
    #             for j in range(i + 1, n):
    #                 if self.is_palin(s, i, j) and j - i + 1 > lps[-1]:
    #                     lps = (i, j, j - i + 1)
    #         return s[lps[0]:lps[1] + 1]

    #     def is_palin(self, s, l, r):
    #         if l >= r:
    #             return True
    #         while l < r:
    #             if s[l] != s[r]:
    #                 return False
    #             l += 1
    #             r -= 1
    #         return True

    # APP2: iterate center of the palindro, center can be on char or between chars.
    # Then use two pointers of opposite directions
    # Time: O(n^2) space: O(1) Runtime: 68%
    #     def longestPalindrome(self, s: str) -> str:
    #         if not s or len(s) < 2:
    #             return s
    #         start = length = 0
    #         for i in range(len(s) - 1):
    #             count1, start1 = self.get_palindrom_len(s, i, i)
    #             count2, start2 = self.get_palindrom_len(s, i, i + 1)
    #             if count1 > count2 and count1 > length:
    #                 start, length = start1, count1
    #             if count2 > count1 and count2 > length:
    #                 start, length = start2, count2
    #         return s[start:start + length]

    #     def get_palindrom_len(self, s, l, r):
    #         while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
    #             l -= 1
    #             r += 1
    #         return (r - l - 1, l + 1)

    # APP3: DP. dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
    # dp[i][i] == True, dp[i][i - 1] = True. calculate col by col
    # Time: O(n^2) space: O(n^2) Runtime: 37%
    # def longestPalindrome(self, s: str) -> str:
    #     n, max_len, start = len(s), 1, 0
    #     if not s or n < 2:
    #         return s
    #     dp = [[True] * n for _ in range(n)]
    #     for j in range(1, n):
    #         for i in range(0, j):
    #             dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
    #             if dp[i][j] and j - i + 1 > max_len:
    #                 max_len, start = j - i + 1, i
    #     return s[start:start + max_len]

    # APP4: DP rolling array to optimize APP3
    # Time: O(n^2) space: O(n) Runtime: 41%
    # def longestPalindrome(self, s: str) -> str:
    #     n, max_len, start = len(s), 1, 0
    #     if not s or n < 2:
    #         return s
    #     old, new = [True] * n, [True] * n
    #     for j in range(1, n):
    #         for i in range(0, j):
    #             new[i] = old[i + 1] and s[i] == s[j]
    #             if new[i] and j - i + 1 > max_len:
    #                 max_len, start = j - i + 1, i
    #         old, new = new, old
    #     return s[start:start + max_len]

    # APP5: Manacher
    # Time: O(n) space: O(n) Runtime: 97%
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        s = "#" + "#".join(list(s)) + "#"
        n, max_right, start, max_len, arm_len, j = len(s), -1, 1, 0, [], -1
        for i in range(n):
            if i <= max_right:
                i_mirror = i - 2 * (i - j)
                min_arm_len = min(arm_len[i_mirror], max_right - i)
                cur_arm_len = self.find_arm_len(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.find_arm_len(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > max_right:
                j = i
                max_right = i + cur_arm_len

            if 2 * cur_arm_len > max_len:
                max_len = 2 * cur_arm_len
                start = i - cur_arm_len
        return s[start + 1:start + max_len:2]

    def find_arm_len(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return ((right - 1) - (left + 1)) // 2





