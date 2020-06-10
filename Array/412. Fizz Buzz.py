class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]
    
    def fizzBuzz(self, n: int) -> List[str]:
        if not n or n < 0:
            return []
        res = []
        for i in range(1, n + 1):
            cur = ""
            if not i % 3:
                cur += "Fizz"
            if not i % 5:
                cur += "Buzz"
            if not i % 3 or not i % 5:
                res.append(cur)
            else:
                res.append(str(i))
        return res
