# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# corner case:
# 1. only one node
# 2. only two nodes
# 3. even
# 4. odd
# input: 1-2-3-4
#          h c n
# revsersed: 1-2-4-3
# merged: 1-4-2-3
class Solution:
    def reorderList(self, n1: ListNode) -> None:
        if not n1:
            return
        # find mid of the list
        s, f = n1, n1.next
        while f and f.next:
            s, f = s.next, f.next.next

        n2 = self.reverse(s)
        # merge
        self.merge(n1, n2)

    def reverse(self, head):
        pre, cur = None, head.next
        while cur:
            next = cur.next
            cur.next = pre
            pre, cur = cur, next
        head.next = None
        return pre

    def merge(self, n1, n2):
        l1, l2, cur = n1, n2, ListNode(-1)
        while l1 and l2 and l1 != n2:
            l1_next, l2_next = l1.next, l2.next
            cur.next = l1
            cur = cur.next
            cur.next = l2
            cur = cur.next
            l1, l2 = l1_next, l2_next
        while l1:
            cur.next = l1
            cur, l1 = cur.next, l1.next
        while l2:
            cur.next = l2
            cur, l2 = cur.next, l2.next

        #     def reorderList(self, n1: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if not n1:
#             return
#         pre_info, left = {}, n1
#         while n1 and n1.next:
#             pre_info[n1.next] = n1
#             n1 = n1.next
#         right = n1

#         while left.next and left.next is not right:
#             # insersion
#             left_next = left.next
#             left.next, right.next = right, left_next

#             # remove right at the end
#             pre_info[right].next = None

#             # update left and right
#             left, right = left_next, pre_info[right]

