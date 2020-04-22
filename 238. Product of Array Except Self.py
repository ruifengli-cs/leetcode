# Brute force: for each item, loop through array and find other's product. O(n^2)
# Optimization: use an array to store prefix product, then loop array backwards. O(n)
# Optimization: use two arrays, one for prefix product, one for suffix product. 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        prefix_produc = [1] * len(nums)
        ans = [1] * len(nums)
        # get prefix sum 
        for i in range(len(nums)):
            if i == 0:
                prefix_produc[i] = nums[i]
                continue
            prefix_produc[i] = prefix_produc[i - 1] * nums[i]
        
        suffix_product = 1
        for j in range(len(nums) - 1, -1, -1):
            if j == 0:
                ans[j] = suffix_product
                continue
            ans[j] = suffix_product * prefix_produc[j - 1]
            suffix_product *= nums[j]
        return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        prefix_product, suffix_product, ans = [1] * n, [1] * n, [1] * n
        for i in range(n): 
            if i == 0:
                prefix_product[i] = nums[i]
                continue
            prefix_product[i] = prefix_product[i - 1] * nums[i]
            
        for j in range(n - 1, - 1, -1):
            if j == n - 1:
                suffix_product[j] = nums[j]
                continue
            suffix_product[j] = suffix_product[j + 1] * nums[j]    
        
        for i in range(n):
            if i > 0:
                ans[i] *= prefix_product[i - 1]
            if i < n - 1:
                ans[i] *= suffix_product[i + 1]
        return ans
        
