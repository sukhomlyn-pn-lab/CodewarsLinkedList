"""Linked Lists - Recursive Reverse"""
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head:Node):
    new_list = None
    def go_to_next(node:Node):
        if node.next is not None:
            go_to_next(node.next)
        if new_list is None:
            new_list = node
            curr = new_list
        else:
            curr.next = node
            curr = curr.next
    return new_list
