class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """

    # def findWords(self, str, dict):
    #     if not str or not dict:
    #         return []
    #     mapping = collections.defaultdict(list)
    #     res = []
    #     for index, ch in enumerate(str):
    #         mapping[ch].append(index)

    #     for word in dict:
    #         cur_str = cur_word = 0
    #         while cur_str < len(str) and cur_word < len(word):
    #             ch =  word[cur_word]
    #             if ch not in mapping:
    #                 break
    #             index = self.find(ch, mapping, cur_str)
    #             if index == -1:
    #                 break
    #             cur_str = index + 1
    #             cur_word += 1
    #         if cur_word == len(word):
    #             res.append(word)
    #     return res

    # def find(self, ch, mapping, cur_str):
    #     array = mapping[ch]
    #     n = len(array)
    #     start, end = 0, n - 1
    #     while start + 1 < end:
    #         mid = start + (end - start) // 2
    #         if array[mid] < cur_str:
    #             start = mid
    #         else:
    #             end = mid
    #     if array[start] >= cur_str:
    #         return array[start]
    #     if array[end] >= cur_str:
    #         return array[end]
    #     return -1

    def findWords(self, str, dict):
        if not str or not dict:
            return []
        n, res = len(str), []
        mapping = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(26):
                if ord(str[i]) - ord('a') == j:
                    mapping[i][j] = i
                else:
                    mapping[i][j] = mapping[i + 1][j]

        for word in dict:
            cur_str = cur_word = 0
            while cur_word < len(word) and cur_str < len(str):
                ch = word[cur_word]
                index = mapping[cur_str][ord(ch) - ord('a')]
                if index == n:
                    break
                cur_str = index + 1
                cur_word += 1
            if cur_word == len(word):
                res.append(word)
        return res


class Solution:
    """
    @param str: the string
    @param dict: the dictionary
    @return: return words which  are subsequences of the string
    """

    # assumption: all chars are lowercase.
    # n = len(str), m = avg len of word, k = len(dict)
    # APP1: two pointers to match each word.
    # Time: O(nmk) space: O(1)

    # APP2: use defaultdict to store str char: [idx] mapping.
    # Time: O(mk * lgn) space: O(n)

    # APP3: use 2D list idx: [26] to find next char index in O(1)
    # Time: O(mk) space: O(n)
    def findWords(self, str, dict):
        if not str or not dict:
            return []
        n = len(str)
        data, res = self.build_data(str), []
        for word in dict:
            idx_str = idx_word = 0
            for ch in word:
                found_idx = data[idx_str][ord(ch) - ord('a')]
                if found_idx == n:
                    continue
                idx_str = found_idx + 1
                idx_word += 1

            if idx_word == len(word):
                res.append(word)
        return res

    # go backwards to build data in O(n)
    def build_data(self, str):
        n = len(str)
        data = [[n] * 26 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(26):
                data[i][j] = data[i + 1][j]
                if ord(str[i]) - ord('a') == j:
                    data[i][j] = i
        return data