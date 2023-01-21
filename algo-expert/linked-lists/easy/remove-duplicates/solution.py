class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    curr = linkedList
    visited = set()
    while curr.next:
        visited.add(curr.value)
        if curr.next.value in visited:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return linkedList
