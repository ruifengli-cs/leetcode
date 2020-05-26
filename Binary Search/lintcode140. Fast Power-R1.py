class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
# APP1: brute force: multiply one by one recursively
Time: O(n) space: O(1) stack depth = O(n) Runtime: maximum recursion depth exceeded
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
        return (a * self.fastPower(a, b, n - 1)) % b
    
# APP2: brute force: multiply one by one iteratively
# Time: O(n) space: O(1) Runtime: TLE
    def fastPower(self, a, b, n):
        # bug need to check if n == 0
        if n == 0:
            return 1 % b
        power = 1
        for i in range(n):
            power = (power * a) % b
        return power
    
# APP3: binary search multiply recursively
# Time: O(lgn) space: O(1)
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
        power = self.fastPower(a, b, n // 2)
        ans = power * power
        if n % 2 != 0:
            ans = (ans * a) % b
        return ans % b

# APP4: binary search iterative approach to multiply exponentially
# 比如 n=5,可以看做 a^{(101)} % b 5的二进制是101）
# 而 a 的幂次我们只需要知道 a^1, a^{(10)}, a^{(100)}... 也就是 a^1, a^2, a^4...
# 因此不断的把 a = a * a 就可以了
# Time: O(lgn) space: O(1)
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= a
            a = a * a % b
            n = n // 2
        return ans % b
        
