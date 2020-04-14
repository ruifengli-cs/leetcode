class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
# a ** n = a * a * a * a * a * ....* a (n times)= a^2 * a^2 *..*a^2(n/2 times)
# a ** n = (a ** n/2) ^ 2 
# APP1: recursion
    def fastPower(self, a, b, n):
        if n < 0:
            a = 1 / a 
        if n == 0:
            return 1 % b
        ans = self.dfs(a, b, n)
        return ans
    
    def dfs(self, a, b, n):
        if n == 0:
            return 1 
        if n % 2 != 0:
            return self.dfs(a, b, n // 2) ** 2 * a % b
        return self.dfs(a, b, n // 2) ** 2 % b

# APP1: another implementation
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
        power = self.fastPower(a, b, n // 2)
        ans = power * power % b
        if n % 2 != 0:
            ans = ans * a % b
        return ans    
        
# APP2: iterative
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b 
        base = a 
        ans = 1 
        while n > 0:
            if n % 2 != 0:
                ans = ans * base % b
            n = n // 2 
            base = base * base 
        return ans
