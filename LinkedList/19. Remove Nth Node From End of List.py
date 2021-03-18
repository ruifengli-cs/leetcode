# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# APP1: fast, slow pointers
# Time: O(n) one pass. space: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        slow = fast = dummy
        dummy.next = head
        while fast.next and n:
            fast = fast.next
            n -= 1
        if n > 0:
            return None
        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next
        return dummy.next