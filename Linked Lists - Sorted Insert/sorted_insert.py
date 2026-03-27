"""Linked Lists - Sorted Insert"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head:Node, data):
    if head is None:
        return Node(data)
    curr = head
    if data<=curr.data:
        head = Node(data)
        head.next = curr
        return head
    while curr is not None:
        if curr.next is None or curr.next.data>=data:
            next_el = curr.next
            new_el = Node(data)
            new_el.next = next_el
            curr.next = new_el
            break
        curr = curr.next
    return head
