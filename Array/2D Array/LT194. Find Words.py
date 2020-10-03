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