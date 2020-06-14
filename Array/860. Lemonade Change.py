class Solution:
    # APP1: naive approach. use list of 3 count bills. if bill is 5, then take it, if 10, see if have at least one 5, if 20,
    # see if have one 5 and one 10 or three 5s.
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return True
        counter = [0] * 3
        for bill in bills:
            if bill == 5:
                counter[0] += 1
            elif bill == 10:
                if counter[0] <= 0:
                    return False
                counter[0] -= 1
                counter[1] += 1
            elif bill == 20:
                if counter[1] > 0 and counter[0] > 0:
                    counter[0] -= 1
                    counter[1] -= 1
                    counter[2] += 1
                    continue
                if counter[0] > 2:
                    counter[0] -= 3
                    counter[2] += 1
                    continue
                return False
        return True

    # APP2: use two variables to track 5 and 10s.
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five, ten = five - 1, ten + 1
            elif ten:
                ten, five = ten - 1, five - 1
            else:
                five -= 3
            if five < 0:
                return False
        return True

    def lemonadeChange(self, bills):
        five = ten = 0
        for num in bills:
            if num == 5:
                five += 1
            elif num == 10 and five:
                ten += 1
                five -= 1
            elif num == 20 and five and ten:
                five -= 1
                ten -= 1
            elif num == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True
