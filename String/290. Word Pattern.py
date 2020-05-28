class Solution:
    # use hashmap to store key: pattern char, value: str word. if key existes and value not equal, return false
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern or not str:
            return False
        str_list = str.split(' ')
        mapping = {}
        n, m = len(pattern), len(str_list)
        uniq_val = set()
        if n != m:
            return False
        for i in range(n):
            if pattern[i] in mapping:
                if mapping[pattern[i]] != str_list[i]:
                    return False
            else:
                mapping[pattern[i]] = str_list[i]
                if str_list[i] in uniq_val:
                    return False
                uniq_val.add(str_list[i])
        return True

    # APP2: zip them as tuple, compare the length of it. should be all unique
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_list = str.split(" ")
        return len(set(zip(pattern, str_list))) == len(set(str_list)) == len(set(pattern)) and len(str_list) == len(
            pattern)