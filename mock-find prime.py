https://leetcode.com/problems/count-primes/

# Count the number of prime numbers less than a non-negative number, n.
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# n can be negative, 0, 1 is not prime numbers
# Prime: only can be divided by 1 or itself

# n < 0: return 0
# if n == 0 or 1 return 0
# 3, 4, 5, 6


# 2-itself - 1
# Time: O(n^2) Space: O(1)
# count = 0
# for i in range(2, n + 1) 
#     if self.is_prime(i):
#         count += 1
# return count

class Solution:
    def countPrimes(self, n: int) -> int:
        if n is None or n < 2:
            return 0
        count = 0 if n < 2 else 1
        for i in range(1, n + 1, 2):
            if i == 1:
                continue
            if self.is_prime2(i):
                count += 1
        return count
    
    def is_prime(self, i):
        for j in range(2, i):
            if i % j == 0:
                return False
        return True
    
    def is_prime2(self, i):
        for j in range(2, int(i ** 0.5 ) + 1):
            if i % j == 0:
                return False
        return True

# 2 - sqrt(n) 
# 1. 2 * i mark False
# 2. i * i mark False
# need to mark all prime 倍数
# 3. count how many True

# n = 100
# 0 - 10
# all even number mark as False
# all sqr number mark as False

    # def countPrimes(self, n: int) -> int:
    #     if n is None or n < 2:
    #         return 0
    #     res = [True] * (n + 1)
    #     res[0], res[1] = False, False
    #     for i in range(2, ):
    #         if i
        

# O(n/2 * sqrt(n/2))
# 3,5,7,9,11
# 10
# 2,4 -> 8,10
# 3,9 -> 


# 8 = 2*4
# O(1) is_prime
# 1,2,3,4,---16
# f,f,f,t,
# 16 = 4 * 4 = 2 * 8,       0-4
# Approach2: if i is not a prime, i1 * i2 = i, if i1 == i2,  2 - sqrt(i)
# O(n * sqrt(n))


class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        """1 is True, 0 is False"""
        is_prime = [1 for i in range(n-1)] # from 1 to n-1
        is_prime[0] = 0 # 1 is not prime
        
        
        """outer loop upper bound pow(n,0.5)+1
        is based upon inner loop, considering all squares already
        """ 
        # i == 3, is_prime[2] 3 is prime, 9 - 100,          
        for i in range(2,int(n**0.5)+1): 
            if is_prime[i-1]:
                """previous number has covered all the multiples
                so pow(i,2) is the starting point, and interval i"""
                for j in range(i**2,n,i):
                    is_prime[j-1] = 0
        
        return sum(is_prime)
sol = Solution()
print(sol.countPrimes(20000000))
