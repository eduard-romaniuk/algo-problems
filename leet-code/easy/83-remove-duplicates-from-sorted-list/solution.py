from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        while tail:
            curr = tail
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            tail = curr.next
        return head
