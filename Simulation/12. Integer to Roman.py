# 1 2 3   4  5 6 7 8   9
# I      IV  V         IX

# 10 20 30   40  50 60 70 80 90
# X          XL  L           XC

# 100 200 300 400 500 600 700 800 900
# C           CD   D              CM

# 1000 2000 ......
# M

class Solution:
    def intToRoman(self, num: int) -> str:
        if not num:
            return ""
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        reps = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = []
        for i in range(len(numbers)):
            if num >= numbers[i]:
                count = num // numbers[i]
                num -= count * numbers[i]
                res.append(reps[i] * count)
        return ''.join(res)