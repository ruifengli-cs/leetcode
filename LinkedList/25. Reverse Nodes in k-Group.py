# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# APP1: iterative way
# first: check if after p it contains k group, if yes, reverse k group, return h, t
# second: p.next = h, t.next = c
# p        c
# d - 1-2-3-4-5， k = 3
# d - 3-2-1-4-5

# Time: O(n) space: O(1)
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        cur = dummy = ListNode(-1)
        cur.next = head
        while cur:
            # first: check if after p it contains k group,
            p, count = cur, 0
            while p and count < k:
                p, count = p.next, count + 1
            if not p:
                break
            next_head = p.next
            # if yes, reverse k group, return h, t
            h, t = self.reverse(cur.next, k)
            cur.next, t.next, cur = h, next_head, t
        return dummy.next

    def reverse(self, head, k):
        dummy = prev = ListNode(-1)
        cur, count = head, 0
        while cur and count < k:
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
            count += 1
        return prev, head