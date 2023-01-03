class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1, list2):
    tail = head = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            tail = tail.next
            list1 = list1.next
        else:
            tail.next = list2
            tail = tail.next
            list2 = list2.next

    tail.next = list1 if list1 else list2
    return head.next
