# arr = [1, 0, 1, 1, 0, 1]
#              l
#                    r
#       
#                        l       
#                        r 
# max_length: 1
# max_length: track current max length of consecutive ones
# find the longest consecutive ones and return the length
# assumption: only 0, 1 in the array.

# approach1: brute force. nested for loop to find all the subarray: O(n^2)
# check who has the longest consecutive ones. O(n)
# Time: O(n^3)



# approach2: two pointers + max_length
# Time: O(n) Space: O(1)

class Solution:
    def find_logest_ones(self, arr):
        if not arr:
            return 0
        left = right = 0
        max_length = 0
        n = len(arr)
        
        while left < n and right < n:
            while left < n and arr[left] == 0:
                left += 1
            right = left
            while right < n and arr[right] == 1:
                right += 1
            max_length = max(max_length, right - left)
            left = right
        return max_length
array = [0,0,0,0,1,1,1,1,0,1,1,1]
sol = Solution()
print(sol.find_logest_ones(array))

# follow up: delete only one zero or not delete any
[0,0,0,0,1,1,1,1,0,1,1,1]                 
# pre-fix max length array at current index
# suffix max length array at current index
# update max_length
[0,0,0,0,1,1,1,1,0,1,1,1]   (arr, k)
                 i
f[8][3] = max(f[8][2], )
k, index
define: f[i][k]: max length at index i with k operations already operformed
        
f[i][k] = max(f[i][k - 1] + 1, f[i][k]) 


if (nums[i]==0) {       j = 0 - k        
     dp[i][k] = dp[i-1][j-1]+1;
     dp[i][0] = 0;                
 }
 else {
     dp[i][0] = dp[i-1][0]+1;
     dp[i][1] = dp[i-1][1]+1;
 }
