"""Linked Lists - Get Nth Node"""


class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node:Node, index:int):
    if not isinstance(node, Node) or not isinstance(index, int):
        raise ValueError("")
    curr = node
    count = 0
    while curr is not None:
        if count == index:
            return curr
        count+=1
        curr = curr.next
    raise ValueError("")
