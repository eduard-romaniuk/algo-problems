class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


def reverse_list(head):
    previous = None
    current = head
    while current is not None:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
    return previous
