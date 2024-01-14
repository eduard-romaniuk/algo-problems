from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_next():
            nonlocal l1, l2
            res = 0
            if l1:
                res += l1.val
                l1 = l1.next
            if l2:
                res += l2.val
                l2 = l2.next
            return res

        head = tail = None
        remainder = 0
        while l1 or l2:
            sum = get_next() + remainder
            digit = sum % 10
            remainder = sum // 10
            if not tail:
                head = tail = ListNode(digit)
            else:
                tail.next = ListNode(digit)
                tail = tail.next
        if remainder > 0:
            tail.next = ListNode(remainder)
        return head
