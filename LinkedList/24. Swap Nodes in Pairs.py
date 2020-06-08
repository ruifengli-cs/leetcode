# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# d-1-2-3-4
# p c n
#   ||
#   \/
# d-2-1-3-4
#     p c n
# pre.next, cur.next = next, next.next (d-2, 1-3)
# next.next = cur (2-1)
# update all the pointers
# pre = cur
# cur = pre.next
# next = cur.next if cur is not None

# Time: O(n) space: O(1) runtime: 11% memory: 6%
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # set dummy as second node
        dummy = ListNode(-1)
        pre, cur, next = dummy, head, head.next
        while next:
            # swap cur and next
            pre.next, cur.next = next, next.next
            next.next = cur
            # update all pointers
            pre = cur
            cur = pre.next
            if not cur:
                return dummy.next
            next = cur.next
        return dummy.next

    # APP2: recursion, only swap first one and second one, and recursively call it
    # Time: O(n) Space: O(n//2) for stack
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first, second = head, head.next
        first.next = self.swapPairs(second.next)
        second.next = first
        return second

    # APP3: same as APP2 but one line. before: first, second, third, after: second, first, third recursion
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            head, head.next, head.next.next = head.next, head, self.swapPairs(head.next.next)
        return head