# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# proof: 2(a + b) = a + b + n * cycle =>  a + b = n * cycle =>  a = (n - 1)*cycle + c => a = c if you start at Z

#     a      b
# X ------Y-----Z
#         |     |
#         -------
#            c

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        # check cycle, if exist, return meet point
        meet_point = self.check_cycle(head)
        if not meet_point:
            return None
        while meet_point != head:
            meet_point = meet_point.next
            head = head.next
        return head

    def check_cycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None