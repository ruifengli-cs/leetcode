class Solution:
    # APP1: reversed the list, use carry to process it digit by digit, then reverse it back
    # Pros: can use same approach for linkedlist, Cons: additional space for list
    # Time: O(n) Space: O(n) Runtime: 6% memory: 5%
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        reversed_digits = digits[::-1]
        carry, n = 1, len(digits)
        for i in range(n):
            cur = reversed_digits[i] + carry
            reversed_digits[i] = (cur) % 10
            carry = cur // 10
        if carry:
            reversed_digits.append(carry)
        reversed_digits.reverse()
        return reversed_digits

    # APP2: convert list to number, convert it to string, then break down to list
    # Time: O(n) Space: O(n) Runtime: 10% memory: 5%
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        num, n = 0, len(digits)
        for i in range(n):
            num += digits[i] * pow(10, n - 1 - i)
        return [d for d in str(num + 1)]

    # APP3: process it backwards in-place.
    # case1: if digit is not 9, plus 1 then return.
    # case2: if digit is 9: set cur digit to 0, next digit plus 1 then return
    # case3: if all digits are 9, create new n + 1 array
    # Time: O(n) sapce: O(1) for most case, O(n) for only input is all 9s
    # Runtime: 33% memory: 5%
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return 0
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # if digits[i] == 9
            digits[i] = 0

        # if input is all 9s like 999999
        return [1] + [0] * n

    # APP4: one line using map
    def plusOne(self, digits: List[int]) -> List[int]:
        return map(int, list(str(int(''.join(map(str, digits))) + 1)))