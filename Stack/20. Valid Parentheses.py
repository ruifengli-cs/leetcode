class Solution:
    # APP1: use stack.
    # Time: O(n) space: O(n) Runtime: 95%
    # def isValid(self, s: str) -> bool:
    #     if not s:
    #         return True
    #     stack = []
    #     for ch in s:
    #         if ch in ['(', '{', '[']:
    #             stack.append(ch)
    #             continue
    #         if ch == ')':
    #             if not stack or stack[-1] != '(':
    #                 return False
    #             stack.pop()
    #         if ch == '}':
    #             if not stack or stack[-1] != '{':
    #                 return False
    #             stack.pop()
    #         if ch == ']':
    #             if not stack or stack[-1] != '[':
    #                 return False
    #             stack.pop()
    #     return True if not stack else False

    # APP2: use stack and dict for more consise version
    # Time: O(n) space: O(n) Runtime: 95%
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack, data = [], {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in data:
                if not stack or stack[-1] != data[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return False if stack else True