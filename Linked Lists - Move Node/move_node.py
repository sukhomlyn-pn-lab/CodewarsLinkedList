"""Linked Lists - Move Node"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source:Node, dest:Node):
    first_el = source
    source = source.next
    first_el.next = dest
    dest = first_el

    return Context(source, dest)
