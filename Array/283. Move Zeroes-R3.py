class Solution:
    # attempt1: sort it then reverse it, Pros: in-place. Cons: no maintain relative order
    # Time: O(nlgn) Space: O(1) if use list.reverse(), O(n) if use list[::-1]

    # attempt2: Two pointers in opposite direction, swap 0 to the right. no maintain relative order
    # Time: O(n), space: O(1)

    # attempt3: create new array to get ans, not in-place
    # Time: O(n), space: O(n)

    # APP1: based on attempt3, I can loop through new array and overwrite old array
    # Time: O(n), space: O(n). Operations: O(n)
    # Runtime: 52% Memory: 5%
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return
        new_nums = [0] * len(nums)
        i = 0
        for num in nums:
            if num != 0:
                new_nums[i] = num
                i += 1
        for i in range(len(nums)):
            nums[i] = new_nums[i]
        return

    # APP2:Two pointers in same direction, swap 0 and none 0s, in-place, with relative order
    # Time: O(n), space: O(1). Operations: [0,1,0,1] 4 times
    # Runtime: 91% memory: 5%
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return
        slow = fast = 0
        n = len(nums)
        # skip none 0, move slow to first 0         
        while fast < n and nums[fast] != 0:
            fast += 1
            slow += 1
        while fast < n:
            #           move fast to fist none 0
            while fast < n and nums[fast] == 0:
                fast += 1
            if fast < n:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1
        return

    # APP3: Two pointers in same direction, overwrite none-zero first half and zero second half
    # Time; O(n), space: O(1). Operations: [0,1,0,1] 2 times. Optimal
    # Runtime: 99%, memory: 5%
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums:
            return
        # Bug forget to define n
        n = len(nums)
        slow = fast = 0
        while fast < n and nums[fast] != 0:
            fast += 1
            slow += 1
        while fast < n:
            while fast < n and nums[fast] == 0:
                fast += 1
            if fast == n:
                break
            if nums[slow] != nums[fast]:
                nums[slow] = nums[fast]
            slow += 1
            fast += 1
        while slow < n:
            if nums[slow] != 0:
                nums[slow] = 0
            slow += 1
        return
