"""Parse a linked list from a string"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
def linked_list_from_string(list_repr: str) -> Node | None:
    if not isinstance(list_repr, str) or list_repr == 'None':
        return None
    list_repr = list_repr.split(' -> ')
    head = Node(int(list_repr[0]))
    prev = head
    for el in list_repr[1:-1]:
        prev.next = Node(int(el))
        prev = prev.next
    return head
