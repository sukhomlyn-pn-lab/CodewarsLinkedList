"""Linked Lists - Push & BuildOneTwoThree"""



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head:Node, data):
    value = Node(data)
    value.next = head
    return value

def build_one_two_three():
    value = None
    for data in range(3, 0, -1):
        value = push(value, data)

    return value
