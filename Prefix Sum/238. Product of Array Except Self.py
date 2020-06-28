class Solution:
# APP1: brute force, multiply all others except itself
# Time: O(n^2) space: O(1) Runtime: TLE
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        res = []
        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                product *= nums[j]
            res.append(product)
        return res
            
# APP2: preprocess array to get prefix product, then loop back
# Time: O(n) Space: O(n) Runtime: 92% Memory: 90%
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        prefix = self.get_prefix_product(nums)
        n = len(nums)
        res = [1] * n
        post_prod = 1
        for i in range(n - 1, -1, -1):
            product = post_prod * prefix[i]
            res[i] = product
            post_prod *= nums[i]
        return res
        
    def get_prefix_product(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pre_prod = nums[0]
        for i in range(1, n):
            res[i] = pre_prod
            pre_prod *= nums[i]
        return res

# APP3: preprocess both prefix and suffix
# Time: O(n) space: O(n) Runtime: 47% Memory: 30%
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        prefix = self.get_prefix_prod(nums)
        reversed_nums = nums[::-1]
        suffix = self.get_prefix_prod(reversed_nums)
        suffix.reverse()
        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        return res
        
    def get_prefix_prod(self, nums):
        n = len(nums)
        prod = 1
        res = []
        for i in range(n):
            res.append(prod)
            prod *= nums[i]
        return res
    
# APP4: optimize APP2 by operating on the prefix array directly without allocation new array
# Time: O(n) Space: O(1) Runtime: 92% memory: 86%
#     input:       [1,2,3,4]
#     prefix_prod: [1,1,2,6]
#     suffix_prod: [24,12,4,1]
#     output:      [24,12,8,6]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        prefix = self.get_prefix_prod(nums)
        prod = 1
        for i in range(n - 1, -1, -1):
            prefix[i] *= prod
            prod *= nums[i]
        return prefix
    
    def get_prefix_prod(self, nums):
        n = len(nums)
        prod = 1
        res = []
        for i in range(n):
            res.append(prod)
            prod *= nums[i]
        return res
