# non negative numbers, integer k
# check if the list has continious subarray at lease two elements, the sum of subarray is n * k
# input: arr: List[int], k: int
# output: bool
# if the list sorted? no
# range for k? 0, -1, 1, 32bit
# length of the list: 0 - 10 ^ 4

# eg. [1,4,2,3,5], k = 3
# 4 + 2 = 6

# Solution1:
# brute force: find all subarrays and see if any sum can be divided by k
# Time: O(n^2) space: O(1)

# solution2:
# prefix sum for every index, try every pos, find all subarray's sum
# Time: O(n^2) space: O(n)

# k=3
# a - b = n*k
# -> (a - b) % k = 0
# a % k = b % k

# [1,0,0]
# k = 0
# presum = [1,1,1]
# uniq: 1:0


# k = 0
# k < 0, n < 0

class Solution:
    def sub_sum(self, arr, k) -> bool:
        if not arr:
            return False
        presum, n, now_sum, uniq = [], len(arr), 0, {0: -1}
        for num in arr:
            now_sum += num
            presum.append(now_sum)

        for i in range(n):
            if k == 0:
                if presum[i] in uniq:
                    if i - uniq[presum[i]] > 1:
                        return True
                    continue
                uniq[presum[i]] = i
                continue

            val = presum[i] % k
            if val in uniq and i - uniq[val] > 1:
                return True
            uniq[val] = i
        return False


sol = Solution()
arr = [1, 0, 0, 0, 1]
print(sol.sub_sum(arr, 0))